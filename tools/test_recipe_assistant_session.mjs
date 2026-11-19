import test from "node:test";
import assert from "node:assert/strict";
import {createCookingSession,createManualTimer} from "../assets/recipe-assistant-session.mjs";

const recipe=()=>({id:"REC-0017",ingredients:[{position:0,raw:"sal"},{position:1,raw:"sal"}],steps:[{order:1},{order:2}]});
test("checklist reversible por ocurrencia y sin mutación",()=>{
  const source=recipe(), original=structuredClone(source), s=createCookingSession(source);
  s.markIngredient(1,true);s.markIngredient(1,true);
  assert.deepEqual(s.snapshot().prepared,[1]);
  s.markIngredient(0,true);s.markIngredient(1,false);
  assert.deepEqual(s.snapshot().prepared,[0]);
  assert.deepEqual(source,original);
  s.snapshot().prepared.push(99);assert.deepEqual(s.snapshot().prepared,[0]);
});
test("navegación y finalización independientes",()=>{
  const s=createCookingSession(recipe());
  assert.equal(s.move(-1).current,1);
  assert.equal(s.move(1).current,2);
  assert.equal(s.move(1).current,2);
  assert.deepEqual(s.snapshot().completed,[]);
  s.markStep(2,true);s.move(-1);s.markStep(1,true);s.markStep(2,false);
  assert.deepEqual(s.snapshot().completed,[1]);assert.equal(s.snapshot().current,1);
});
test("reinicio y aislamiento",()=>{
  const s=createCookingSession(recipe());s.markIngredient(0,true);s.markStep(1,true);s.move(1);
  assert.deepEqual(s.reset(),createCookingSession(recipe()).snapshot());
  s.markIngredient(1,true);
  assert.deepEqual(createCookingSession(recipe()).snapshot().prepared,[]);
});
test("receta vacía y entradas inválidas",()=>{
  const s=createCookingSession({id:"REC-X",ingredients:[],steps:[]});
  assert.equal(s.move(1).current,null);
  assert.throws(()=>s.markStep(1,true));assert.throws(()=>s.markIngredient(0,true));
  assert.throws(()=>s.move(2));
  assert.throws(()=>createCookingSession({id:"X",ingredients:[{position:1}],steps:[]}));
  assert.throws(()=>createCookingSession({id:"X",ingredients:[],steps:[{order:0}]}));
  assert.throws(()=>createCookingSession(recipe()).markIngredient(0,"true"));
});
test("temporizador: plazo absoluto incluso entre actualizaciones",()=>{
  let now=0;const t=createManualTimer(()=>now);
  assert.equal(t.start(1,5).remainingSeconds,65);
  now=1001;assert.equal(t.snapshot().remainingMs,63999);
  assert.equal(t.snapshot().remainingSeconds,64);
  now=65000;assert.deepEqual(t.snapshot(),{status:"finished",remainingMs:0,remainingSeconds:0});
  now=100000;assert.equal(t.snapshot().status,"finished");
  assert.equal(t.start(0,3).status,"running");
});
test("pausa, reanudación y cancelación",()=>{
  let now=100;const t=createManualTimer(()=>now);
  t.start(0,10);now=2600;assert.equal(t.pause().remainingMs,7500);
  now=60000;assert.equal(t.snapshot().remainingMs,7500);
  t.resume();now=67500;assert.equal(t.snapshot().status,"finished");
  t.cancel();assert.deepEqual(t.snapshot(),{status:"idle",remainingMs:0,remainingSeconds:0});
  t.start(0,1);t.cancel();assert.equal(t.resume().status,"idle");
});
test("pausa después del plazo no revive el temporizador",()=>{
  let now=0;const t=createManualTimer(()=>now);t.start(0,1);
  now=2000;assert.equal(t.pause().status,"finished");assert.equal(t.resume().status,"finished");
});
test("validación de duración y reloj",()=>{
  let now=0;const t=createManualTimer(()=>now);
  for(const [m,s] of [[0,0],[-1,1],[0,60],[1.2,1],[1440,0],[NaN,1],["1",1]])
    assert.throws(()=>t.start(m,s));
  assert.equal(t.start(1439,59).remainingSeconds,86399);
  assert.throws(()=>t.start(0,2));now=-1;assert.throws(()=>t.snapshot());
});
test("temporizador independiente de navegación y estado culinario",()=>{
  let now=0;const t=createManualTimer(()=>now),s=createCookingSession(recipe());
  t.start(0,3);s.move(1);s.markStep(2,true);now=3000;t.snapshot();
  assert.deepEqual(s.snapshot().completed,[2]);assert.equal(s.snapshot().current,2);
});
