import test from "node:test";
import assert from "node:assert/strict";
import {emptyShopping,addList,addItem,markPurchased,prepareTransfer,recordTransferCompleted} from "../assets/culinary-shopping-model.mjs";
import {createShoppingPersistence,parseBackup,serializeBackup,STORAGE_KEY,MAX_JSON_LENGTH} from "../assets/culinary-shopping-persistence.mjs";
const item={id:"a",name:"Arroz",quantity:"1.50",unit:"kg",category:null,notes:null,purchased:false,provenance:null,transfer:null};
const populated=()=>addItem(addList(emptyShopping(),"l","Compra"),"l",item);
const target={id:"shopping-a",name:"Arroz",quantity:"1.50",unit:"kg",category:null,notes:null,location:"pantry",date:null,date_type:null};
const pending=()=>prepareTransfer(markPurchased(populated(),"l","a",true),"l","a",target);
const complete=()=>recordTransferCompleted(pending(),"l","a",target);
function fixture(initial=null){
  const values=new Map([["novacoquinaria.culinary-pantry","independent"]]);
  if(initial!==null)values.set(STORAGE_KEY,initial);
  const storage={getItem:k=>values.get(k)??null,setItem:(k,v)=>values.set(k,v)};
  return {storage,values,get raw(){return storage.getItem(STORAGE_KEY);},set raw(v){if(v===null)values.delete(STORAGE_KEY);else values.set(STORAGE_KEY,v);},adapter:createShoppingPersistence(()=>storage)};
}
const rejects=(fn,code)=>assert.throws(fn,e=>e.code===code);
test("ausencia, guardado, recarga y clave independiente",()=>{
  const f=fixture();assert.deepEqual(f.adapter.load(),{status:"absent",data:emptyShopping()});assert.equal(f.raw,null);
  assert.deepEqual(f.adapter.save(populated()),populated());
  assert.deepEqual(createShoppingPersistence(()=>f.storage).load(),{status:"loaded",data:populated()});
  assert.equal(f.values.get("novacoquinaria.culinary-pantry"),"independent");
});
test("formato o versión incompatibles no se sobrescriben",()=>{
  for(const [raw,code] of [["{","invalid"],['{"schema_version":"9","lists":[]}',"version"],["null","invalid"],['{"schema_version":"0.1.0","entries":[]}',"invalid"]]){
    const f=fixture(raw);rejects(()=>f.adapter.load(),code);rejects(()=>f.adapter.save(populated()),"not_ready");assert.equal(f.raw,raw);
  }
});
test("acceso bloqueado y lectura fallida",()=>{
  rejects(()=>createShoppingPersistence(()=>{throw Error();}).load(),"blocked");
  const f=fixture();f.storage.getItem=()=>{throw Error();};rejects(()=>f.adapter.load(),"read");
});
test("cuota y escritura fallida preservan copia válida",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const raw=f.raw;
  f.storage.setItem=()=>{const e=Error();e.name="QuotaExceededError";throw e;};
  rejects(()=>f.adapter.save(emptyShopping()),"quota");assert.equal(f.raw,raw);
  f.storage.setItem=()=>{throw Error();};rejects(()=>f.adapter.save(emptyShopping()),"write");
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),populated());
});
test("cambio externo sin evento bloquea escritura",()=>{
  const f=fixture();f.adapter.load();const other=createShoppingPersistence(()=>f.storage);other.load();other.save(populated());
  rejects(()=>f.adapter.save(emptyShopping()),"conflict");assert.deepEqual(f.adapter.load().data,populated());
});
test("eventos de Pantry no bloquean Shopping; clear sí",()=>{
  const f=fixture();f.adapter.load();
  assert.equal(f.adapter.observeStorageEvent({key:"novacoquinaria.culinary-pantry",newValue:"x"}),false);
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:{}}),false);
  assert.equal(f.adapter.observeStorageEvent({key:null,storageArea:f.storage}),true);
  rejects(()=>f.adapter.save(populated()),"conflict");f.adapter.load();
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:f.storage}),true);
});
test("previsualización con dos recuentos, cancelación y sustitución",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const raw=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyShopping()));
  assert.equal(preview.listCount,0);assert.equal(preview.itemCount,0);
  assert.equal(f.adapter.confirmImport(preview,false).status,"cancelled");assert.equal(f.raw,raw);
  rejects(()=>f.adapter.confirmImport({...preview,itemCount:1},true),"invalid");
  rejects(()=>f.adapter.previewImport("{}"),"invalid");
  assert.deepEqual(f.adapter.confirmImport(preview,true),{status:"imported",data:emptyShopping()});
});
test("importación no descarta ni altera registros vigentes",()=>{
  for(const document of [pending(),complete()]){
    const f=fixture();f.adapter.load();f.adapter.save(document);const raw=f.raw;
    for(const copy of [emptyShopping(),populated()]){
      rejects(()=>f.adapter.confirmImport(f.adapter.previewImport(serializeBackup(copy)),true),"transfer_history");
      assert.equal(f.raw,raw);
    }
    const alternate=document.lists[0].items[0].transfer.state==="pending"?complete():pending();
    rejects(()=>f.adapter.confirmImport(f.adapter.previewImport(serializeBackup(alternate)),true),"transfer_history");
    assert.deepEqual(f.adapter.confirmImport(f.adapter.previewImport(serializeBackup(document)),true).data,document);
  }
});
test("fallo o conflicto al importar conserva documento",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const raw=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyShopping()));
  f.storage.setItem=()=>{throw Error();};rejects(()=>f.adapter.confirmImport(preview,true),"write");assert.equal(f.raw,raw);
  f.raw=null;rejects(()=>f.adapter.confirmImport(preview,true),"conflict");assert.equal(f.raw,null);
});
test("exportación conserva registros y última copia válida",()=>{
  const f=fixture();rejects(()=>f.adapter.exportLastValid(),"not_ready");f.adapter.load();f.adapter.save(complete());
  const copy=f.adapter.snapshot();copy.lists[0].items[0].transfer.entry.name="Otro";
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),complete());
  f.raw="invalid";rejects(()=>f.adapter.load(),"invalid");assert.deepEqual(parseBackup(f.adapter.exportLastValid()),complete());
});
test("límite JSON y validación del esquema",()=>{
  rejects(()=>parseBackup(" ".repeat(MAX_JSON_LENGTH+1)),"invalid");rejects(()=>parseBackup(42),"invalid");
  assert.deepEqual(parseBackup(serializeBackup(populated())),populated());
});
