import test from "node:test";
import assert from "node:assert/strict";
import {scalingBasis,scaleIngredient} from "../assets/recipe-assistant-scaling.mjs";
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
test("rechaza intervalos, aproximaciones, medidas y valores inseguros",()=>{
  const entry=item();
  for(const quantity of [
    {...entry.quantity,status:"range",max:"400"},
    {...entry.quantity,approximate:true},
    {...entry.quantity,unit:"unidad"},
    {...entry.quantity,unit:"cucharada"},
    {...entry.quantity,min:"1/2",max:"1/2"},
    {...entry.quantity,min:"Infinity",max:"Infinity"},
    {...entry.quantity,status:"ambiguous"}
  ]) assert.equal(scaleIngredient({...entry,quantity},4,6),null);
  for(const target of [0,25,1.5,NaN]) assert.equal(scaleIngredient(entry,4,target),null);
});
