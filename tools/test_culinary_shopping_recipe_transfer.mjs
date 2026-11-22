import test from "node:test";
import assert from "node:assert/strict";
import {createRecipeSelection,putRecipeSelection,takeRecipeSelection,RECIPE_TRANSFER_KEY} from "../assets/culinary-shopping-recipe-transfer.mjs";
const recipe={id:"REC-0017",title:"Receta",source_commit:"a".repeat(40),ingredients:[{position:0,name:"ajo",raw:"1–2 dientes de ajo",source_location:{start_line:10,end_line:10}},{position:1,name:"arroz",raw:"200 g de arroz",source_location:{start_line:11,end_line:11}}]};
function storage(){const m=new Map();return {getItem:k=>m.get(k)??null,setItem:(k,v)=>m.set(k,v),removeItem:k=>m.delete(k)};}
test("selección concreta y procedencia literal sin cantidades inferidas",()=>{const x=createRecipeSelection(recipe,[1,0]);assert.deepEqual(x.items.map(i=>i.name),["arroz","ajo"]);assert.equal(x.items[1].provenance.raw,"1–2 dientes de ajo");assert.equal(x.items[1].provenance.source_commit,recipe.source_commit);assert.equal(Object.hasOwn(x.items[0],"quantity"),false);});
test("rechaza selección vacía, repetida o inexistente",()=>{for(const p of [[],[0,0],[2],[-1],["0"]])assert.throws(()=>createRecipeSelection(recipe,p));});
test("transporte de un solo uso",()=>{const s=storage(),x=createRecipeSelection(recipe,[0]);assert.equal(takeRecipeSelection(()=>s),null);putRecipeSelection(()=>s,x);assert.deepEqual(takeRecipeSelection(()=>s),x);assert.equal(takeRecipeSelection(()=>s),null);});
test("rechaza datos incompatibles y acceso bloqueado",()=>{const s=storage();s.setItem(RECIPE_TRANSFER_KEY,"{}");assert.throws(()=>takeRecipeSelection(()=>s));assert.equal(s.getItem(RECIPE_TRANSFER_KEY),null);assert.throws(()=>putRecipeSelection(()=>{throw Error();},createRecipeSelection(recipe,[0])));});

test("cantidades adaptadas propuestas para revisión, conservando procedencia",()=>{
  const source=structuredClone({...recipe,yield:{min:"4",max:"4",unit:"racion"},ingredients:[
    {...recipe.ingredients[0],quantity:{status:"exact",min:"2",max:"2",unit:"diente",approximate:false}},
    {...recipe.ingredients[1],quantity:{status:"exact",min:"200",max:"200",unit:"g",approximate:false}}
  ]});
  const previous=structuredClone(source);
  const result=createRecipeSelection(source,[0,1],{targetServings:6});
  assert.deepEqual(result.items.map(x=>x.suggestion),[
    {quantity:"3",unit:"diente"},{quantity:"300",unit:"g"}
  ]);
  assert.equal(result.items[0].provenance.raw,"1–2 dientes de ajo");
  assert.deepEqual(source,previous);
  const storageInstance=storage();
  putRecipeSelection(()=>storageInstance,result);
  assert.deepEqual(takeRecipeSelection(()=>storageInstance),result);
  assert.throws(()=>createRecipeSelection(source,[0],{targetServings:0}));
  assert.throws(()=>createRecipeSelection(recipe,[0],{targetServings:6}));
});
test("cantidades no escalables no generan propuestas",()=>{
  const source={...recipe,yield:{min:"4",max:"4",unit:"racion"},
    ingredients:[{...recipe.ingredients[0],quantity:{status:"range",min:"1",max:"2",unit:"diente",approximate:false}}]};
  const result=createRecipeSelection(source,[0],{targetServings:6});
  assert.equal(Object.hasOwn(result.items[0],"suggestion"),false);
});
test("rechazo de propuestas manipuladas o incompatibles",()=>{
  const source={...recipe,yield:{min:"4",max:"4",unit:"racion"},
    ingredients:[{...recipe.ingredients[1],position:0,quantity:{status:"exact",min:"200",max:"200",unit:"g",approximate:false}}]};
  const correct=createRecipeSelection(source,[0],{targetServings:6});
  for(const suggestion of [{quantity:"-3",unit:"g"},{quantity:"300",unit:null},
                            {quantity:"300",unit:"g",extra:"x"}]){
    assert.throws(()=>putRecipeSelection(()=>storage(),{...correct,items:[{...correct.items[0],suggestion}]}));
  }
});
