import test from "node:test";
import assert from "node:assert/strict";
import {emptyPlanner,addPlanEntry} from "../assets/culinary-planner-model.mjs";
import {createPlannerPersistence,PlannerStorageError,parseBackup,serializeBackup,STORAGE_KEY,MAX_JSON_LENGTH}
  from "../assets/culinary-planner-persistence.mjs";
const record={id:"meal-1",date:"2026-11-21",meal:"dinner",title:"Café y arroz",notes:"Preparación libre",source:{type:"free_text"}};
const plan=()=>addPlanEntry(emptyPlanner(),record);
function fixture(initial=null){
  const values=new Map([["novacoquinaria.culinary-shopping","shopping"],
    ["novacoquinaria.culinary-pantry","pantry"]]);
  if(initial!==null)values.set(STORAGE_KEY,initial);
  let readFailure=null,writeFailure=null;
  const storage={
    getItem(k){if(readFailure)throw readFailure;return values.get(k)??null;},
    setItem(k,v){if(writeFailure)throw writeFailure;values.set(k,v);}
  };
  const adapter=createPlannerPersistence(()=>storage);
  return {adapter,values,storage,
    set readFailure(value){readFailure=value;},set writeFailure(value){writeFailure=value;},
    get raw(){return values.get(STORAGE_KEY)??null;},
    set raw(value){if(value===null)values.delete(STORAGE_KEY);else values.set(STORAGE_KEY,value);}
  };
}
const rejects=(fn,code)=>assert.throws(fn,e=>e instanceof PlannerStorageError&&e.code===code);
test("clave separada, ausencia sin escritura, guardado y recarga",()=>{
  const f=fixture();assert.deepEqual(f.adapter.load(),{status:"absent",data:emptyPlanner()});
  assert.equal(f.raw,null);assert.deepEqual(f.adapter.save(plan()),plan());
  assert.deepEqual(createPlannerPersistence(()=>f.storage).load().data,plan());
  assert.equal(f.values.get("novacoquinaria.culinary-shopping"),"shopping");
  assert.equal(f.values.get("novacoquinaria.culinary-pantry"),"pantry");
});
test("rechaza versiones, formatos y documentos sin alterarlos",()=>{
  for(const [raw,code] of [["{","invalid"],["null","invalid"],['{"schema_version":"9","entries":[]}',"version"],
     ['{"schema_version":"0.1.0","lists":[]}',"invalid"]]){
    const f=fixture(raw);rejects(()=>f.adapter.load(),code);
    rejects(()=>f.adapter.save(emptyPlanner()),"not_ready");assert.equal(f.raw,raw);
  }
});
test("bloqueo de acceso, fallo de lectura y copia válida recuperable",()=>{
  rejects(()=>createPlannerPersistence(()=>{throw Error();}).load(),"blocked");
  const f=fixture();f.adapter.load();f.adapter.save(plan());
  f.readFailure=new Error("lectura");
  rejects(()=>f.adapter.load(),"read");
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),plan());
  rejects(()=>f.adapter.save(emptyPlanner()),"not_ready");
});
test("fallo de cuota y fallo genérico conservan última versión",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(plan());const original=f.raw;
  f.writeFailure=Object.assign(Error("espacio"),{name:"QuotaExceededError"});
  rejects(()=>f.adapter.save(emptyPlanner()),"quota");
  f.writeFailure=Error("escritura");
  rejects(()=>f.adapter.save(emptyPlanner()),"write");
  assert.equal(f.raw,original);assert.deepEqual(f.adapter.snapshot(),plan());
});
test("conflictos aunque no haya evento y posterior recarga",()=>{
  const f=fixture();f.adapter.load();
  const other=createPlannerPersistence(()=>f.storage);other.load();other.save(plan());
  rejects(()=>f.adapter.save(emptyPlanner()),"conflict");
  assert.deepEqual(f.adapter.load().data,plan());
  assert.deepEqual(f.adapter.save(plan()),plan());
});
test("eventos pertinentes bloquean sin afectar eventos de Shopping y Pantry",()=>{
  const f=fixture();f.adapter.load();
  for(const key of ["novacoquinaria.culinary-shopping","novacoquinaria.culinary-pantry"])
    assert.equal(f.adapter.observeStorageEvent({key,newValue:"cambio",storageArea:f.storage}),false);
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:{}}),false);
  assert.equal(f.adapter.observeStorageEvent({key:STORAGE_KEY,newValue:"x",storageArea:f.storage}),true);
  rejects(()=>f.adapter.save(plan()),"conflict");
  f.adapter.load();
  assert.equal(f.adapter.observeStorageEvent({key:null,storageArea:f.storage}),true);
  rejects(()=>f.adapter.save(plan()),"conflict");
});
test("exportación e importación con previsualización, recuento y cancelación",()=>{
  const f=fixture();rejects(()=>f.adapter.exportLastValid(),"not_ready");
  f.adapter.load();f.adapter.save(plan());const raw=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyPlanner()));
  assert.equal(preview.count,0);assert.equal(f.adapter.confirmImport(preview,false).status,"cancelled");
  assert.equal(f.raw,raw);
  rejects(()=>f.adapter.confirmImport(preview,true),"invalid");
  const nextPreview=f.adapter.previewImport(serializeBackup(emptyPlanner()));
  assert.deepEqual(f.adapter.confirmImport(nextPreview,true),{status:"imported",data:emptyPlanner()});
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),emptyPlanner());
});
test("no se admiten previsualizaciones construidas o de otra sesión",()=>{
  const f=fixture();f.adapter.load();
  const preview=f.adapter.previewImport(serializeBackup(plan()));
  rejects(()=>f.adapter.confirmImport({...preview},true),"invalid");
  const other=createPlannerPersistence(()=>f.storage);other.load();
  rejects(()=>other.confirmImport(preview,true),"invalid");
  assert.equal(f.raw,null);
});
test("fallo o conflicto de importación conserva documento original",()=>{
  const f=fixture();f.adapter.load();f.adapter.save(plan());const original=f.raw;
  const preview=f.adapter.previewImport(serializeBackup(emptyPlanner()));
  f.writeFailure=Error("fallo");
  rejects(()=>f.adapter.confirmImport(preview,true),"write");
  assert.equal(f.raw,original);
  f.writeFailure=null;f.raw=null;
  rejects(()=>f.adapter.confirmImport(preview,true),"conflict");
  assert.equal(f.raw,null);
  assert.deepEqual(f.adapter.snapshot(),plan());
});
test("copias profundas, referencias históricas y notas sobreviven",()=>{
  const f=fixture();f.adapter.load();
  const recipe={id:"meal-2",date:"2026-11-23",meal:"lunch",title:"Ternera",
    notes:"Sin calcular ingredientes",source:{type:"recipe",recipe_id:"REC-0190",
      source_commit:"a".repeat(40),source_path:"07_Cocina_Asiatica/ternera.md"}};
  const content=addPlanEntry(plan(),recipe);
  f.adapter.save(content);
  const clone=f.adapter.snapshot();clone.entries[1].source.recipe_id="REC-0000";
  assert.deepEqual(parseBackup(f.adapter.exportLastValid()),content);
  assert.deepEqual(createPlannerPersistence(()=>f.storage).load().data,content);
});
test("límites, JSON inválido y error de serialización",()=>{
  rejects(()=>parseBackup(" ".repeat(MAX_JSON_LENGTH+1)),"invalid");
  rejects(()=>parseBackup(7),"invalid");
  rejects(()=>parseBackup("{"),"invalid");
  rejects(()=>serializeBackup({schema_version:"9",entries:[]}),"invalid");
  assert.deepEqual(parseBackup(serializeBackup(plan())),plan());
});
