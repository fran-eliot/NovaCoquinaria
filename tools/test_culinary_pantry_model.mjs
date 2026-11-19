import test from "node:test";
import assert from "node:assert/strict";
import {emptyPantry,validatePantry,validateEntry,addEntry,editEntry,removeEntry,
  filterEntries,selectedMentions,validDate,dateRelation,MAX_ENTRIES} from "../assets/culinary-pantry-model.mjs";

const entry=(id="a",extra={})=>({id,name:"Arroz",quantity:"1.50",unit:"kg",category:"Cereales",location:"pantry",date_type:null,date:null,notes:null,...extra});
test("lotes separados y operaciones inmutables",()=>{
  const initial=emptyPantry(),one=addEntry(initial,entry()),two=addEntry(one,entry("b",{location:"freezer"}));
  assert.equal(initial.entries.length,0);assert.equal(one.entries.length,1);assert.equal(two.entries.length,2);
  const edited=editEntry(two,"a",entry("a",{quantity:"0.25"}));
  assert.equal(two.entries[0].quantity,"1.50");assert.equal(edited.entries[0].quantity,"0.25");
  assert.deepEqual(removeEntry(edited,"b").entries,[edited.entries[0]]);
  assert.throws(()=>addEntry(two,entry()));assert.throws(()=>editEntry(two,"a",entry("c")));
  assert.throws(()=>removeEntry(two,"missing"));
});
test("cantidades literales y ausencias",()=>{
  for(const q of ["0.000001","999999999.123456","1.50"])assert.equal(validateEntry(entry("a",{quantity:q})).quantity,q);
  assert.equal(validateEntry(entry("a",{quantity:null,unit:null})).quantity,null);
  for(const q of ["0","0.000000","-1","1e3","1,2","01","1/2","1.0000001","1000000000",1,NaN])
    assert.throws(()=>validateEntry(entry("a",{quantity:q})));
  assert.throws(()=>validateEntry(entry("a",{quantity:null})));
  assert.throws(()=>validateEntry(entry("a",{unit:null})));
});
test("fechas civiles reales y tipos diferenciados",()=>{
  for(const date of ["2000-02-29","2024-02-29","0001-01-01","9999-12-31"])assert.equal(validDate(date),true);
  for(const date of ["1900-02-29","2026-02-29","2026-04-31","0000-01-01","2026-1-1","2026-11-00",null])assert.equal(validDate(date),false);
  assert.equal(validateEntry(entry("a",{date:"2026-11-19",date_type:"best_before"})).date_type,"best_before");
  assert.throws(()=>validateEntry(entry("a",{date:"2026-11-19"})));
  assert.throws(()=>validateEntry(entry("a",{date_type:"expiry"})));
  assert.throws(()=>validateEntry(entry("a",{date:"2026-11-19",date_type:"unknown"})));
});
test("relación temporal sin inferencia",()=>{
  const today="2026-11-19";
  assert.equal(dateRelation("2026-11-18",today),"past");
  assert.equal(dateRelation(today,today),"today");
  assert.equal(dateRelation("2026-11-20",today),"future");
  assert.equal(dateRelation(null,today),"undated");
  assert.throws(()=>dateRelation(null,"invalid"));
});
test("campos y límites estrictos",()=>{
  for(const extra of [{name:""},{name:" arroz "},{name:"a".repeat(161)},{id:"../a"},{location:"unknown"},{notes:"a".repeat(1001)},{category:3},{name:"a\nb"},{unexpected:true}])
    assert.throws(()=>validateEntry(entry("a",extra)));
  assert.equal(validateEntry(entry("a",{notes:"Primera línea\nSegunda línea"})).notes,"Primera línea\nSegunda línea");
  assert.throws(()=>validatePantry({schema_version:"9.0.0",entries:[]}));
  assert.throws(()=>validatePantry({...emptyPantry(),entries:Array(MAX_ENTRIES+1).fill(entry())}));
  assert.throws(()=>validatePantry({...emptyPantry(),entries:[entry(),entry()]}));
});
test("filtros acumulables, Unicode y orden original",()=>{
  const data={...emptyPantry(),entries:[entry("a",{name:"Cafe\u0301",category:"Bebidas",date:"2026-11-18",date_type:"expiry"}),entry("b",{name:"Café",category:"Bebidas",location:"fridge"}),entry("c")]};
  assert.deepEqual(filterEntries(data,{name:"CAFÉ"}).map(e=>e.id),["a","b"]);
  assert.deepEqual(filterEntries(data,{name:"café",category:"bebidas",location:"fridge",relation:"undated",today:"2026-11-19"}).map(e=>e.id),["b"]);
  assert.deepEqual(filterEntries(data,{relation:"past",today:"2026-11-19"}).map(e=>e.id),["a"]);
  assert.deepEqual(filterEntries(data,{name:"nada"}),[]);
  assert.equal(filterEntries(data).length,3);
});
test("selección explícita de nombres, sin cantidades ni unión de lotes",()=>{
  const data={...emptyPantry(),entries:[entry("a"),entry("b",{name:"ARROZ"}),entry("c",{name:"ajo"}),entry("d",{name:"---"})]};
  assert.deepEqual(selectedMentions(data,["c","a","b"]),["ajo","Arroz"]);
  for(const ids of [[],["missing"],["a","a"],["d"]])assert.throws(()=>selectedMentions(data,ids));
  assert.equal(data.entries.length,4);
});
test("validación devuelve copias y no modifica el origen",()=>{
  const source={...emptyPantry(),entries:[entry()]};
  const validated=validatePantry(source);validated.entries[0].name="Otro";
  assert.equal(source.entries[0].name,"Arroz");
});
