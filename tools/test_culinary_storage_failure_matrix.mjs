import test from "node:test";
import assert from "node:assert/strict";
import {emptyShopping,addList,addItem,markPurchased,prepareTransfer} from "../assets/culinary-shopping-model.mjs";
import {emptyPantry} from "../assets/culinary-pantry-model.mjs";
import {emptyPlanner,addPlanEntry} from "../assets/culinary-planner-model.mjs";
import {createShoppingPersistence,STORAGE_KEY as S,serializeBackup as shoppingJSON} from "../assets/culinary-shopping-persistence.mjs";
import {createPantryPersistence,STORAGE_KEY as P,serializeBackup as pantryJSON} from "../assets/culinary-pantry-persistence.mjs";
import {createPlannerPersistence,STORAGE_KEY as L,serializeBackup as plannerJSON} from "../assets/culinary-planner-persistence.mjs";
import {transferPurchased,recoverTransfer} from "../assets/culinary-shopping-pantry-coordinator.mjs";

const item={id:"a",name:"Arroz",quantity:null,unit:null,category:null,notes:null,purchased:false,provenance:null,transfer:null};
const lot={id:"shopping-a",name:"Arroz",quantity:"2",unit:"kg",category:null,
  location:"pantry",date_type:null,date:null,notes:null};
const planEntry={id:"meal-a",date:"2026-11-21",meal:"lunch",title:"Arroz",
  notes:null,source:{type:"free_text"}};
const baseShopping=()=>markPurchased(addItem(addList(emptyShopping(),"list","Semanal"),
  "list",item),"list","a",true);
const basePlan=()=>addPlanEntry(emptyPlanner(),planEntry);
const requires=(operation,code)=>assert.throws(operation,error=>error?.code===code);
function fixture(){
  const values=new Map(),writes=[],reads=[];
  let denyRead=()=>false,denyWrite=()=>null;
  const storage={
    getItem(key){reads.push(key);if(denyRead(key))throw Error("No read");return values.get(key)??null;},
    setItem(key,raw){
      const reason=denyWrite(key,raw);
      if(reason){const error=Error("Write rejected");if(reason==="quota")error.name="QuotaExceededError";throw error;}
      writes.push(key);values.set(key,raw);
    },
    removeItem(key){values.delete(key);}
  };
  const shopping=()=>createShoppingPersistence(()=>storage);
  const pantry=()=>createPantryPersistence(()=>storage);
  const planner=()=>createPlannerPersistence(()=>storage);
  const prepare=()=>{
    const sh=shopping(),pa=pantry(),pl=planner();
    sh.load();pa.load();pl.load();
    const expected=sh.save(baseShopping());
    pl.save(basePlan());
    writes.length=0;
    return {shopping:sh,pantry:pa,planner:pl,expected,
      args:{shopping:sh,pantry:pa,expected,listId:"list",itemId:"a",entry:lot,confirmed:true}};
  };
  return {values,writes,reads,storage,shopping,pantry,planner,prepare,
    blockRead:fn=>{denyRead=fn;},blockWrite:fn=>{denyWrite=fn;},
    raw:key=>values.get(key)??null,
    restore:(key,raw)=>{if(raw===null)values.delete(key);else values.set(key,raw);}
  };
}
const transferState=shopping=>shopping.load().data.lists[0].items[0].transfer?.state??null;
const recover=(f,sh,pa)=>recoverTransfer({shopping:sh,pantry:pa,
  expected:sh.load().data,listId:"list",itemId:"a",confirmed:true});

test("almacenamientos independientes y una restauración no reescribe las otras claves",()=>{
  const f=fixture(),x=f.prepare(),before=[f.raw(S),f.raw(P),f.raw(L)];
  const preview=x.planner.previewImport(plannerJSON(emptyPlanner()));
  assert.equal(x.planner.confirmImport(preview,false).status,"cancelled");
  assert.deepEqual([f.raw(S),f.raw(P),f.raw(L)],before);
  const imported=x.planner.previewImport(plannerJSON(emptyPlanner()));
  assert.equal(x.planner.confirmImport(imported,true).status,"imported");
  assert.equal(f.raw(S),before[0]);assert.equal(f.raw(P),before[1]);
  assert.equal(f.planner().load().data.entries.length,0);
});
test("evento de otra clave no bloquea guardado; cambio de la misma clave sí",()=>{
  const f=fixture(),x=f.prepare();
  assert.equal(x.shopping.observeStorageEvent({key:L,storageArea:f.storage,newValue:"x"}),false);
  assert.equal(x.planner.observeStorageEvent({key:P,storageArea:f.storage,newValue:"x"}),false);
  assert.equal(x.pantry.observeStorageEvent({key:S,storageArea:f.storage,newValue:"x"}),false);
  const external=f.shopping();external.load();external.save(emptyShopping());
  requires(()=>x.shopping.save(baseShopping()),"conflict");
  assert.deepEqual(f.shopping().load().data,emptyShopping());
  assert.deepEqual(f.planner().load().data,basePlan());
});
test("cuota, lectura y escritura fallidas no silencian conflictos ni sustituyen documentos",()=>{
  for(const key of [S,P,L]){
    const f=fixture(),x=f.prepare();
    const adapter=key===S?x.shopping:key===P?x.pantry:x.planner;
    const value=key===S?baseShopping():key===P?emptyPantry():basePlan();
    const baseline=f.raw(key);
    f.blockWrite(k=>k===key?"quota":null);
    requires(()=>adapter.save(value),"quota");
    assert.equal(f.raw(key),baseline);
    f.blockWrite(k=>k===key?"write":null);
    requires(()=>adapter.save(value),"write");
    assert.equal(f.raw(key),baseline);
    f.blockWrite(()=>null);
    f.blockRead(k=>k===key);
    requires(()=>adapter.save(value),"read");
    f.blockRead(()=>false);
    assert.equal(f.raw(key),baseline);
  }
});
test("documentos incompatibles impiden nueva escritura sin alterar el valor inválido",()=>{
  for(const key of [S,P,L]){
    const f=fixture(),x=f.prepare();
    const damaged='{"schema_version":"999","entries":[]}';
    f.restore(key,damaged);
    const target=key===S?f.shopping():key===P?f.pantry():f.planner();
    requires(()=>target.load(),"version");
    requires(()=>target.save(key===S?baseShopping():key===P?emptyPantry():basePlan()),"not_ready");
    assert.equal(f.raw(key),damaged);
  }
});
test("una restauración Shopping que elimina historial protegido es rechazada",()=>{
  const f=fixture(),x=f.prepare();
  transferPurchased(x.args);
  const sh=f.shopping();sh.load();
  const before=f.raw(S),other=[f.raw(P),f.raw(L)];
  const preview=sh.previewImport(shoppingJSON(emptyShopping()));
  requires(()=>sh.confirmImport(preview,true),"transfer_history");
  assert.equal(f.raw(S),before);
  assert.deepEqual([f.raw(P),f.raw(L)],other);
});
test("fallo antes del lote deja intención; recuperación no crea destinos ausentes",()=>{
  const f=fixture(),x=f.prepare();
  f.blockWrite(k=>k===P?"write":null);
  assert.throws(()=>transferPurchased(x.args));
  f.blockWrite(()=>null);
  assert.equal(transferState(f.shopping()),"pending");
  const before=[f.raw(S),f.raw(P),f.raw(L)],writes=f.writes.length;
  assert.throws(()=>recover(f,f.shopping(),f.pantry()));
  assert.deepEqual([f.raw(S),f.raw(P),f.raw(L)],before);
  assert.equal(f.writes.length,writes);
});
test("fallo después del lote permite completar la intención sin duplicarlo",()=>{
  const f=fixture(),x=f.prepare();
  f.blockWrite((key,raw)=>key===S&&raw.includes('"completed"')?"write":null);
  assert.throws(()=>transferPurchased(x.args));
  f.blockWrite(()=>null);
  const record=f.raw(P);
  assert.equal(transferState(f.shopping()),"pending");
  const result=recover(f,f.shopping(),f.pantry());
  assert.equal(result.status,"completed");
  assert.equal(f.raw(P),record);
  assert.equal(f.pantry().load().data.entries.length,1);
  assert.equal(transferState(f.shopping()),"completed");
});
test("la restauración independiente de Pantry no reconstruye un lote perdido",()=>{
  const f=fixture(),x=f.prepare();
  f.blockWrite((key,raw)=>key===S&&raw.includes('"completed"')?"write":null);
  assert.throws(()=>transferPurchased(x.args));
  f.blockWrite(()=>null);
  const shoppingBefore=f.raw(S),plannerBefore=f.raw(L);
  const pantryStore=f.pantry();pantryStore.load();
  const preview=pantryStore.previewImport(pantryJSON(emptyPantry()));
  assert.equal(pantryStore.confirmImport(preview,true).status,"imported");
  assert.deepEqual(f.pantry().load().data,emptyPantry());
  const frozen=f.raw(P),writes=f.writes.length;
  assert.throws(()=>recover(f,f.shopping(),f.pantry()));
  assert.equal(f.writes.length,writes);
  assert.equal(f.raw(P),frozen);assert.equal(f.raw(S),shoppingBefore);assert.equal(f.raw(L),plannerBefore);
});
test("lote divergente y fallo de lectura bloquean recuperación sin corregir datos",()=>{
  for(const mode of ["changed","blocked"]){
    const f=fixture(),x=f.prepare();
    f.blockWrite((key,raw)=>key===S&&raw.includes('"completed"')?"write":null);
    assert.throws(()=>transferPurchased(x.args));f.blockWrite(()=>null);
    if(mode==="changed"){
      const pantry=f.pantry();pantry.load();
      pantry.save({schema_version:"0.1.0",entries:[{...lot,name:"Otro"}]});
    }else f.blockRead(key=>key===P);
    const before=[f.raw(S),f.raw(P),f.raw(L)],writes=f.writes.length;
    assert.throws(()=>recover(f,f.shopping(),f.pantry()));
    assert.deepEqual([f.raw(S),f.raw(P),f.raw(L)],before);
    assert.equal(f.writes.length,writes);
  }
});
test("documento esperado obsoleto no crea intención ni altera un lote existente",()=>{
  const f=fixture(),x=f.prepare();
  const other=f.shopping();other.load();other.save(emptyShopping());
  const before=[f.raw(S),f.raw(P),f.raw(L)],writes=f.writes.length;
  assert.throws(()=>transferPurchased(x.args));
  assert.deepEqual([f.raw(S),f.raw(P),f.raw(L)],before);assert.equal(f.writes.length,writes);
});
test("historial completed tras restaurar Pantry vacío no acredita existencias actuales",()=>{
  const f=fixture(),x=f.prepare();transferPurchased(x.args);
  const final=f.raw(S);
  const pantry=f.pantry();pantry.load();
  pantry.confirmImport(pantry.previewImport(pantryJSON(emptyPantry())),true);
  assert.equal(transferState(f.shopping()),"completed");
  assert.deepEqual(f.pantry().load().data.entries,[]);
  assert.equal(f.raw(S),final);
  // La protección del historial no pretende reconciliar ambos documentos.
});
