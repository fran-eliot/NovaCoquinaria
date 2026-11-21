import test from "node:test";
import assert from "node:assert/strict";
import {SELECTION_KEY,validateSelection,storeSelection,consumeSelection,selectCatalogRecord}
  from "../assets/culinary-planner-recipe-transfer.mjs";
const recipe={id:"REC-0017",title:"Arroz con verduras",source_path:"01_Arroces/arroz.md",href:"01_Arroces/arroz.html"};
const catalog={source_commit:"a".repeat(40),recipes:[recipe]};
function store(){const map=new Map();return {getItem:k=>map.get(k)??null,setItem:(k,v)=>map.set(k,v),removeItem:k=>map.delete(k)};}
test("selección mínima explícita, de un solo uso",()=>{
  const storage=store();
  assert.equal(consumeSelection(()=>storage),null);
  storeSelection(()=>storage,"REC-0017");
  assert.equal(storage.getItem(SELECTION_KEY),'{"recipe_id":"REC-0017"}');
  assert.deepEqual(consumeSelection(()=>storage),{recipe_id:"REC-0017"});
  assert.equal(consumeSelection(()=>storage),null);
});
test("rechaza payloads contaminados y IDs inválidos",()=>{
  for(const value of [{recipe_id:"REC-0017",title:"Falso"},{recipe_id:"../../foo"},{},"REC-0017",null])
    assert.throws(()=>validateSelection(value));
  const storage=store();storage.setItem(SELECTION_KEY,'{"recipe_id":"REC-0017","title":"Inyectado"}');
  assert.throws(()=>consumeSelection(()=>storage));
  assert.equal(storage.getItem(SELECTION_KEY),null);
});
test("solo registro único del catálogo vigente, sin atribución de título enviada",()=>{
  assert.deepEqual(selectCatalogRecord(catalog,"REC-0017"),{...recipe,source_commit:"a".repeat(40)});
  assert.throws(()=>selectCatalogRecord(catalog,"REC-9999"));
  assert.throws(()=>selectCatalogRecord({...catalog,recipes:[recipe,recipe]},"REC-0017"));
});
test("rutas, commit y destinos incoherentes no se convierten en enlaces",()=>{
  for(const r of [{...recipe,source_path:"../fuera.md"},{...recipe,href:"https://bad.example"},
    {...recipe,href:"01_Arroces/otro.html"},{...recipe,source_path:"01_Arroces/%2e%2e.md"},
    {...recipe,title:""}])
    assert.throws(()=>selectCatalogRecord({...catalog,recipes:[r]},"REC-0017"));
  assert.throws(()=>selectCatalogRecord({...catalog,source_commit:"bad"},"REC-0017"));
});
test("almacenamiento bloqueado no acepta selección silenciosamente",()=>{
  assert.throws(()=>storeSelection(()=>{throw Error("blocked");},"REC-0017"));
  assert.throws(()=>consumeSelection(()=>{throw Error("blocked");}));
});
