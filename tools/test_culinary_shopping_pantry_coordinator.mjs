import test from "node:test";
import assert from "node:assert/strict";
import {emptyShopping,addList,addItem,markPurchased} from "../assets/culinary-shopping-model.mjs";
import {createShoppingPersistence,STORAGE_KEY as S} from "../assets/culinary-shopping-persistence.mjs";
import {createPantryPersistence,STORAGE_KEY as P} from "../assets/culinary-pantry-persistence.mjs";
import {transferPurchased,recoverTransfer} from "../assets/culinary-shopping-pantry-coordinator.mjs";
const entry={id:"shopping-a",name:"Arroz",quantity:"1",unit:"kg",category:null,notes:null,location:"pantry",date:null,date_type:null};
function fixture(){
  const map=new Map(),writes=[];let reject=()=>false;
  const storage={getItem:k=>map.get(k)??null,setItem(k,v){if(reject(k,v))throw Error("blocked");writes.push(k);map.set(k,v);}};
  const shopping=createShoppingPersistence(()=>storage),pantry=createPantryPersistence(()=>storage);
  shopping.load();const data=shopping.save(markPurchased(addItem(addList(emptyShopping(),"l","Compra"),"l",{id:"a",name:"Arroz",quantity:"1",unit:"kg",category:null,notes:null,purchased:false,provenance:null,transfer:null}),"l","a",true));
  writes.length=0;
  return {shopping,pantry,data,writes,map,block:f=>{reject=f;},args:{shopping,pantry,expected:data,listId:"l",itemId:"a",entry,confirmed:true}};
}
const state=f=>f.shopping.load().data.lists[0].items[0].transfer?.state??null;
test("intención antes de lote y finalización comprobada",()=>{const f=fixture();assert.equal(transferPurchased(f.args).status,"completed");assert.deepEqual(f.writes,[S,P,S]);assert.equal(state(f),"completed");assert.deepEqual(f.pantry.load().data.entries,[entry]);assert.throws(()=>transferPurchased({...f.args,expected:f.shopping.load().data}));});
test("cancelación sin escrituras",()=>{const f=fixture();assert.equal(transferPurchased({...f.args,confirmed:false}).status,"cancelled");assert.deepEqual(f.writes,[]);});
test("fallo al guardar intención no toca Pantry",()=>{const f=fixture();f.block(k=>k===S);assert.throws(()=>transferPurchased(f.args));assert.equal(f.map.has(P),false);assert.equal(state(f),null);});
test("fallo de escritura en Pantry conserva intención y no repite",()=>{const f=fixture();f.block(k=>k===P);assert.throws(()=>transferPurchased(f.args));assert.equal(state(f),"pending");f.block(()=>false);assert.throws(()=>recoverTransfer({...f.args,expected:f.shopping.load().data}));assert.equal(f.map.has(P),false);});
test("fallo al finalizar recuperable sin otro lote",()=>{const f=fixture();f.block((k,v)=>k===S&&v.includes('"completed"'));assert.throws(()=>transferPurchased(f.args));assert.equal(state(f),"pending");f.block(()=>false);const expected=f.shopping.load().data;assert.equal(recoverTransfer({...f.args,expected}).status,"completed");assert.deepEqual(f.writes,[S,P,S]);assert.equal(f.pantry.load().data.entries.length,1);});
test("destino previo incluso idéntico bloquea alta",()=>{const f=fixture();f.pantry.load();f.pantry.save({schema_version:"0.1.0",entries:[entry]});assert.throws(()=>transferPurchased(f.args));assert.equal(state(f),null);assert.equal(f.pantry.load().data.entries.length,1);});
test("destino modificado o borrado no se recrea",()=>{for(const entries of [[],[{...entry,name:"Otro"}]]){const f=fixture();f.block((k,v)=>k===S&&v.includes('"completed"'));assert.throws(()=>transferPurchased(f.args));f.block(()=>false);f.pantry.load();f.pantry.save({schema_version:"0.1.0",entries});assert.throws(()=>recoverTransfer({...f.args,expected:f.shopping.load().data}));assert.equal(state(f),"pending");assert.deepEqual(f.pantry.load().data.entries,entries);}});
test("documento de compras desactualizado y despensa ilegible bloquean",()=>{const f=fixture();assert.throws(()=>transferPurchased({...f.args,expected:emptyShopping()}));f.map.set(P,"invalid");assert.throws(()=>transferPurchased(f.args));assert.equal(state(f),null);assert.equal(f.map.get(P),"invalid");});
