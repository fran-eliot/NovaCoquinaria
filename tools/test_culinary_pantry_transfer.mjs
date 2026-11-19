import test from "node:test";
import assert from "node:assert/strict";
import {putMentions,takeMentions,TRANSFER_KEY} from "../assets/culinary-pantry-transfer.mjs";
function fake(){const m=new Map();return {getItem:k=>m.get(k)??null,setItem:(k,v)=>m.set(k,v),removeItem:k=>m.delete(k)};}
test("selección de un solo uso",()=>{const s=fake();assert.equal(takeMentions(()=>s),null);putMentions(()=>s,["ajo","salsa de soja"]);assert.deepEqual(takeMentions(()=>s),["ajo","salsa de soja"]);assert.equal(takeMentions(()=>s),null);});
test("datos inválidos no se transfieren",()=>{const s=fake();for(const t of [[],[""],["a\nb"],["---"],[2]])assert.throws(()=>putMentions(()=>s,t));s.setItem(TRANSFER_KEY,"{}");assert.throws(()=>takeMentions(()=>s));assert.equal(takeMentions(()=>s),null);});
test("almacenamiento no disponible",()=>{assert.throws(()=>putMentions(()=>{throw Error();},["ajo"]));assert.throws(()=>takeMentions(()=>{throw Error();}));});
