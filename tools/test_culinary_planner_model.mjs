import test from "node:test";
import assert from "node:assert/strict";
import {SCHEMA_VERSION,MAX_ENTRIES,MEALS,emptyPlanner,validatePlanner,validatePlanEntry,
  validCivilDate,shiftCivilDate,weekStart,weekDates,addPlanEntry,editPlanEntry,
  removePlanEntry,filterPlanEntries,entriesForWeek,recipeReferenceStatus}
  from "../assets/culinary-planner-model.mjs";
const source={type:"recipe",recipe_id:"REC-0190",source_commit:"a".repeat(40),source_path:"07_Cocina_Asiatica/ternera.md"};
const entry=(id="a",extra={})=>({id,date:"2026-11-21",meal:"lunch",title:"Arroz",notes:null,source:{type:"free_text"},...extra});
test("fechas gregorianas, bisiestos y límites sin Date ni zona horaria",()=>{
  for(const date of ["0001-01-01","1600-02-29","2000-02-29","2026-11-21","9999-12-31"])assert.equal(validCivilDate(date),true);
  for(const date of ["0000-01-01","1900-02-29","2026-02-29","2026-04-31","9999-13-01","2026-1-02","2026-01-1",null])assert.equal(validCivilDate(date),false);
  assert.equal(shiftCivilDate("2024-02-28",1),"2024-02-29");
  assert.equal(shiftCivilDate("2024-02-29",1),"2024-03-01");
  assert.equal(shiftCivilDate("2023-12-31",1),"2024-01-01");
  assert.equal(shiftCivilDate("0001-01-01",1),"0001-01-02");
  assert.throws(()=>shiftCivilDate("0001-01-01",-1));
  assert.throws(()=>shiftCivilDate("9999-12-31",1));
  assert.throws(()=>shiftCivilDate("2026-11-21",1.5));
});
test("semanas desde lunes, cruces de año y límites del calendario",()=>{
  assert.equal(weekStart("2026-11-21"),"2026-11-16");
  assert.deepEqual(weekDates("2026-11-21"),["2026-11-16","2026-11-17","2026-11-18","2026-11-19","2026-11-20","2026-11-21","2026-11-22"]);
  assert.equal(weekStart("2027-01-01"),"2026-12-28");
  assert.equal(weekDates("2027-01-01")[6],"2027-01-03");
  assert.equal(weekStart("0001-01-01"),"0001-01-01");
  assert.throws(()=>weekDates("9999-12-31"));
});
test("contrato estricto, textos seguros y límites explícitos",()=>{
  const plan=emptyPlanner();assert.equal(plan.schema_version,SCHEMA_VERSION);
  assert.deepEqual(validatePlanner(plan),plan);
  for(const value of ["","a".repeat(161),"<script>\nalert(1)</script>"])assert.throws(()=>validatePlanEntry(entry("a",{title:value})));
  assert.equal(validatePlanEntry(entry("a",{title:"<script>alert(1)</script>"})).title,"<script>alert(1)</script>");
  assert.throws(()=>validatePlanEntry(entry("a",{notes:"\u0000"})));
  assert.throws(()=>validatePlanEntry(entry("a",{date:"2026-02-29"})));
  assert.throws(()=>validatePlanEntry(entry("a",{meal:"brunch"})));
  assert.throws(()=>validatePlanEntry(entry("a",{unknown:1})));
  assert.throws(()=>validatePlanEntry(entry("bad id")));
  assert.equal(MEALS.length,4);
  assert.throws(()=>validatePlanner({schema_version:"0.2.0",entries:[]}));
  assert.throws(()=>validatePlanner({...plan,entries:Array.from({length:MAX_ENTRIES+1},(_,i)=>entry(String(i)))}));
});
test("plato libre distinto de receta, procedencia histórica copiada",()=>{
  const recipe=validatePlanEntry(entry("r",{title:"Ternera",source}));
  assert.deepEqual(recipe.source,source);
  recipe.source.recipe_id="REC-0001";assert.equal(source.recipe_id,"REC-0190");
  const doc=addPlanEntry(emptyPlanner(),entry("r",{source}));
  const copy=validatePlanner(doc);copy.entries[0].source.source_path="mal";
  assert.equal(doc.entries[0].source.source_path,source.source_path);
  for(const bad of [
    {type:"recipe",recipe_id:"REC-0190",source_commit:"a".repeat(40),source_path:"../../secreto.md"},
    {type:"recipe",recipe_id:"REC-0190",source_commit:"a".repeat(40),source_path:"07_Cocina_Asiatica/receta.md?x=y"},
    {type:"recipe",recipe_id:"REC-0190",source_commit:"bad",source_path:"07_Cocina_Asiatica/receta.md"},
    {type:"free_text",recipe_id:"REC-0190"},
    {type:"unknown"},
  ])assert.throws(()=>validatePlanEntry(entry("b",{source:bad})));
});
test("entradas múltiples y orden preservado, operaciones inmutables",()=>{
  const a=addPlanEntry(emptyPlanner(),entry("a"));
  const b=addPlanEntry(a,entry("b",{title:"Ensalada"}));
  assert.deepEqual(b.entries.map(x=>x.id),["a","b"]);
  assert.deepEqual(a.entries.map(x=>x.id),["a"]);
  assert.throws(()=>addPlanEntry(a,entry("a")));
  const c=editPlanEntry(b,"a",entry("a",{date:"2026-11-22",meal:"dinner",notes:"Preparación familiar"}));
  assert.equal(c.entries[0].date,"2026-11-22");assert.equal(b.entries[0].date,"2026-11-21");
  assert.deepEqual(removePlanEntry(c,"b").entries.map(x=>x.id),["a"]);
  assert.throws(()=>removePlanEntry(c,"missing"));
  assert.throws(()=>editPlanEntry(c,"a",entry("c")));
});
test("procedencia inmutable durante edición y sin resolución por título",()=>{
  const a=addPlanEntry(emptyPlanner(),entry("a",{source}));
  assert.deepEqual(editPlanEntry(a,"a",entry("a",{title:"Otro nombre",source})).entries[0].source,source);
  assert.throws(()=>editPlanEntry(a,"a",entry("a",{source:{type:"free_text"}})));
  assert.equal(recipeReferenceStatus(entry("a"),{id:"REC-0190"}),"not_applicable");
  assert.equal(recipeReferenceStatus(entry("a",{source}),null),"unavailable");
  assert.equal(recipeReferenceStatus(entry("a",{source}),{...source,id:source.recipe_id}),"verified");
  assert.equal(recipeReferenceStatus(entry("a",{source}),{...source,id:source.recipe_id,source_commit:"b".repeat(40)}),"changed");
  assert.equal(recipeReferenceStatus(entry("a",{source}),{...source,id:"REC-0099"}),"changed");
});
test("filtros acumulativos, orden de inserción, varias comidas y Unicode",()=>{
  let doc=emptyPlanner();
  doc=addPlanEntry(doc,entry("a",{title:"Café"}));
  doc=addPlanEntry(doc,entry("b",{title:"Cafe\u0301 con leche",meal:"breakfast"}));
  doc=addPlanEntry(doc,entry("c",{title:"Sopa",date:"2026-11-22"}));
  doc=addPlanEntry(doc,entry("d",{title:"CAFÉ",meal:"lunch"}));
  assert.deepEqual(filterPlanEntries(doc,{title:"café"}).map(x=>x.id),["a","b","d"]);
  assert.deepEqual(filterPlanEntries(doc,{title:"café",meal:"lunch"}).map(x=>x.id),["a","d"]);
  assert.deepEqual(filterPlanEntries(doc,{start:"2026-11-22",end:"2026-11-22"}).map(x=>x.id),["c"]);
  assert.deepEqual(entriesForWeek(doc,"2026-11-21").map(x=>x.id),["a","b","c","d"]);
  assert.deepEqual(filterPlanEntries(doc,{title:"No encontrado"}),[]);
  assert.throws(()=>filterPlanEntries(doc,{start:"2026-11-23",end:"2026-11-22"}));
  assert.throws(()=>filterPlanEntries(doc,{meal:"invalid"}));
});
test("referencias no incluyen datos personales en enlaces: el modelo no genera URL",()=>{
  const plan=addPlanEntry(emptyPlanner(),entry("a",{source}));
  assert.equal(Object.hasOwn(plan.entries[0],"href"),false);
  assert.deepEqual(Object.keys(plan.entries[0]).sort(),["date","id","meal","notes","source","title"]);
});
