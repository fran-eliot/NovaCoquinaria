import test from "node:test";
import assert from "node:assert/strict";
import {createRecipeSelection,putRecipeSelection,takeRecipeSelection,RECIPE_TRANSFER_KEY} from "../assets/culinary-shopping-recipe-transfer.mjs";
const recipe={id:"REC-0017",title:"Receta",source_commit:"a".repeat(40),ingredients:[{position:0,name:"ajo",raw:"1–2 dientes de ajo",source_location:{start_line:10,end_line:10}},{position:1,name:"arroz",raw:"200 g de arroz",source_location:{start_line:11,end_line:11}}]};
function storage(){const m=new Map();return {getItem:k=>m.get(k)??null,setItem:(k,v)=>m.set(k,v),removeItem:k=>m.delete(k)};}
test("selección concreta y procedencia literal sin cantidades inferidas",()=>{const x=createRecipeSelection(recipe,[1,0]);assert.deepEqual(x.items.map(i=>i.name),["arroz","ajo"]);assert.equal(x.items[1].provenance.raw,"1–2 dientes de ajo");assert.equal(x.items[1].provenance.source_commit,recipe.source_commit);assert.equal(Object.hasOwn(x.items[0],"quantity"),false);});
test("rechaza selección vacía, repetida o inexistente",()=>{for(const p of [[],[0,0],[2],[-1],["0"]])assert.throws(()=>createRecipeSelection(recipe,p));});
test("transporte de un solo uso",()=>{const s=storage(),x=createRecipeSelection(recipe,[0]);assert.equal(takeRecipeSelection(()=>s),null);putRecipeSelection(()=>s,x);assert.deepEqual(takeRecipeSelection(()=>s),x);assert.equal(takeRecipeSelection(()=>s),null);});
test("rechaza datos incompatibles y acceso bloqueado",()=>{const s=storage();s.setItem(RECIPE_TRANSFER_KEY,"{}");assert.throws(()=>takeRecipeSelection(()=>s));assert.equal(s.getItem(RECIPE_TRANSFER_KEY),null);assert.throws(()=>putRecipeSelection(()=>{throw Error();},createRecipeSelection(recipe,[0])));});
