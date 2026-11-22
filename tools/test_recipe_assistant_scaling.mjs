import test from "node:test";
import assert from "node:assert/strict";
import {scalingBasis,scaleIngredient,formatScaledList} from "../assets/recipe-assistant-scaling.mjs";
const item = (min="320",unit="g") => ({raw:"320 g arroz",quantity:{status:"exact",min,max:min,unit,approximate:false}});
test("rendimiento explícito y único",()=>{
  assert.equal(scalingBasis({yield:{min:"4",max:"4",unit:"racion"}}),4);
  for(const yieldValue of [null,{min:"4",max:"6",unit:"racion"},{min:null,max:null,unit:null},{min:"4",max:"4",unit:"unidad"}])
    assert.equal(scalingBasis({yield:yieldValue}),null);
});
test("escalado reversible de masa y volumen sin alterar el origen",()=>{
  const entry=item(), before=structuredClone(entry);
  assert.deepEqual(scaleIngredient(entry,4,6),{quantity:"480",unit:"g"});
  assert.deepEqual(scaleIngredient(entry,4,4),{quantity:"320",unit:"g"});
  assert.deepEqual(entry,before);
  assert.deepEqual(scaleIngredient(item("1.5","l"),4,6),{quantity:"2,25",unit:"l"});
});
test("fracciones exactas y límites de representación",()=>{
  assert.deepEqual(scaleIngredient(item("1/2","l"),4,6),{quantity:"0,75",unit:"l"});
  assert.deepEqual(scaleIngredient(item("3/4","kg"),3,2),{quantity:"0,5",unit:"kg"});
  assert.deepEqual(scaleIngredient(item("5/2","g"),5,10),{quantity:"5",unit:"g"});
  for(const value of ["0/2","1/0","-1/2","2/3/4","9007199254740993/2"])
    assert.equal(scaleIngredient(item(value),4,6),null);
});
test("unidades contables: solo cantidades enteras positivas",()=>{
  assert.deepEqual(scaleIngredient(item("2","unidad"),4,6),{quantity:"3",unit:"unidad"});
  assert.deepEqual(scaleIngredient(item("4","diente"),4,6),{quantity:"6",unit:"diente"});
  assert.deepEqual(scaleIngredient(item("2","hoja"),4,8),{quantity:"4",unit:"hoja"});
  assert.deepEqual(scaleIngredient(item("1","rama"),2,4),{quantity:"2",unit:"rama"});
  assert.equal(scaleIngredient(item("1","unidad"),4,6),null);
  assert.equal(scaleIngredient(item("1/2","unidad"),4,6),null);
  assert.equal(scaleIngredient(item("1","diente"),4,2),null);
  assert.equal(scaleIngredient(item("3","unidad"),4,2),null);
});
test("rechaza intervalos, aproximaciones, medidas y valores inseguros",()=>{
  const entry=item();
  for(const quantity of [
    {...entry.quantity,status:"range",max:"400"},
    {...entry.quantity,approximate:true},
    {...entry.quantity,unit:"cucharada"},
    {...entry.quantity,min:"Infinity",max:"Infinity"},
    {...entry.quantity,status:"ambiguous"}
  ]) assert.equal(scaleIngredient({...entry,quantity},4,6),null);
  for(const target of [0,25,1.5,NaN]) assert.equal(scaleIngredient(entry,4,target),null);
});

test("lista exportable conserva originales y señala ajustes pendientes",()=>{
  const recipe={title:"Receta de prueba",yield:{min:"4",max:"4",unit:"racion"},ingredients:[
    item("320","g"),item("2","unidad"),{raw:"sal al gusto",quantity:{status:"qualitative"}}
  ]};
  const source=structuredClone(recipe);
  const result=formatScaledList(recipe,6);
  assert.match(result,/Receta de prueba — 6 raciones/);
  assert.match(result,/320 g arroz → 480 g/);
  assert.match(result,/320 g arroz/);
  assert.match(result,/320 g arroz.*480 g/);
  assert.match(result,/320 g arroz/);
  assert.match(result,/sal al gusto \[revisar manualmente\]/);
  assert.deepEqual(recipe,source);
  assert.doesNotMatch(formatScaledList(recipe,4),/\[revisar manualmente\]/);
  assert.throws(()=>formatScaledList(recipe,0));
  assert.throws(()=>formatScaledList({...recipe,yield:null},6));
});
