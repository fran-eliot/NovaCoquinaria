import test from "node:test";
import assert from "node:assert/strict";
import {emptyPantry,addEntry} from "../assets/culinary-pantry-model.mjs";
import {createPantryPersistence,parseBackup,serializeBackup,STORAGE_KEY,MAX_JSON_LENGTH} from "../assets/culinary-pantry-persistence.mjs";

const food={id:"a",name:"Arroz",quantity:"1.50",unit:"kg",category:null,location:"pantry",date_type:null,date:null,notes:null};
const populated=()=>addEntry(emptyPantry(),food);
function fixture(initial=null){
  let raw=initial;
  const storage={getItem(key){assert.equal(key,STORAGE_KEY);return raw;},
    setItem(key,value){assert.equal(key,STORAGE_KEY);raw=value;}};
  return {storage,get raw(){return raw;},set raw(value){raw=value;},adapter:createPantryPersistence(()=>storage)};
}
const rejects=(fn,code)=>assert.throws(fn,e=>e.code===code);
test("clave ausente sin escritura automática; guardar y recargar",()=>{
  const f=fixture();
  assert.deepEqual(f.adapter.load(),{status:"absent",data:emptyPantry()});
  assert.equal(f.raw,null);
  assert.deepEqual(f.adapter.save(populated()),populated());
  assert.deepEqual(createPantryPersistence(()=>f.storage).load(),{status:"loaded",data:populated()});
});
test("documentos incompatibles no se sobrescriben",()=>{
  for(const [raw,code] of [["{","invalid"],['{"schema_version":"9.0.0","entries":[]}',"version"],["null","invalid"],['{"schema_version":"0.1.0","entries":[{}]}',"invalid"]]){
    const f=fixture(raw);rejects(()=>f.adapter.load(),code);rejects(()=>f.adapter.save(populated()),"not_ready");assert.equal(f.raw,raw);
  }
});
test("acceso bloqueado y lectura fallida",()=>{
  rejects(()=>createPantryPersistence(()=>{throw Error();}).load(),"blocked");
  const f=fixture();f.storage.getItem=()=>{throw Error();};rejects(()=>f.adapter.load(),"read");
});
test("cuota y error de escritura conservan la última copia",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const raw=f.raw;
  f.storage.setItem=()=>{const e=Error();e.name="QuotaExceededError";throw e;};
  rejects(()=>f.adapter.save(emptyPantry()),"quota");assert.equal(f.raw,raw);
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),populated());
  f.storage.setItem=()=>{throw Error();};rejects(()=>f.adapter.save(emptyPantry()),"write");
  assert.deepEqual(f.adapter.snapshot(),populated());
});
test("cambio externo bloquea escritura incluso sin evento",()=>{
  const f=fixture();f.adapter.load();const other=createPantryPersistence(()=>f.storage);
  other.load();other.save(populated());rejects(()=>f.adapter.save(emptyPantry()),"conflict");
  assert.deepEqual(f.adapter.load().data,populated());assert.deepEqual(f.adapter.save(emptyPantry()),emptyPantry());
});
test("evento externo y borrado observado requieren recarga",()=>{
  const f=fixture();f.adapter.load();
  assert.equal(f.adapter.observeStorageEvent({key:"other",newValue:"x"}),false);
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:{}}),false);
  assert.equal(f.adapter.observeStorageEvent({key:null,storageArea:f.storage}),true);
  rejects(()=>f.adapter.save(populated()),"conflict");f.adapter.load();
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:f.storage}),true);
});
test("importación validada, cancelación y sustitución explícita",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const previous=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyPantry()));
  assert.equal(preview.count,0);assert.equal(f.adapter.confirmImport(preview,false).status,"cancelled");assert.equal(f.raw,previous);
  rejects(()=>f.adapter.confirmImport({...preview,count:3},true),"invalid");
  rejects(()=>f.adapter.previewImport("{}"),"invalid");assert.equal(f.raw,previous);
  assert.deepEqual(f.adapter.confirmImport(preview,true),{status:"imported",data:emptyPantry()});
});
test("fallo o conflicto al importar no borra el inventario",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(populated());const previous=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyPantry()));
  f.storage.setItem=()=>{throw Error();};rejects(()=>f.adapter.confirmImport(preview,true),"write");assert.equal(f.raw,previous);
  f.raw=null;rejects(()=>f.adapter.confirmImport(preview,true),"conflict");assert.equal(f.raw,null);
});
test("exportación conserva datos originales y distingue ausencia de copia",()=>{
  const f=fixture();rejects(()=>f.adapter.exportLastValid(),"not_ready");f.adapter.load();f.adapter.save(populated());
  const copy=f.adapter.snapshot();copy.entries[0].name="Otro";assert.equal(parseBackup(f.adapter.exportLastValid()).entries[0].name,"Arroz");
  f.raw="invalid";rejects(()=>f.adapter.load(),"invalid");assert.deepEqual(parseBackup(f.adapter.exportLastValid()),populated());
});
test("límite de JSON y formato de esquema",()=>{
  rejects(()=>parseBackup(" ".repeat(MAX_JSON_LENGTH+1)),"invalid");
  rejects(()=>parseBackup(42),"invalid");assert.deepEqual(parseBackup(serializeBackup(populated())),populated());
});
