import test from "node:test";
import assert from "node:assert/strict";
import {emptyShopping,validateShopping,validateItem,addList,renameList,removeList,addItem,editItem,markPurchased,removeItem,filterItems,prepareTransfer,recordTransferCompleted,MAX_LISTS,MAX_ITEMS} from "../assets/culinary-shopping-model.mjs";
const item=(id="a",extra={})=>({id,name:"Arroz",quantity:"1.50",unit:"kg",category:"Cereales",notes:null,purchased:false,provenance:null,transfer:null,...extra});
const initial=()=>addList(emptyShopping(),"l","Compra semanal");
const stocked=()=>addItem(initial(),"l",item());
const origin={recipe_id:"REC-0017",position:0,source_location:{start_line:10,end_line:11},raw:"Arroz 1–2 tazas",source_commit:"a".repeat(40)};
const target=(extra={})=>({id:"shopping-a",name:"Arroz",quantity:"1.50",unit:"kg",category:"Cereales",notes:null,location:"pantry",date:null,date_type:null,...extra});
test("listas independientes, orden y operaciones inmutables",()=>{
  const a=initial(),b=addList(a,"m","Otra compra"),c=renameList(b,"m","Mercado");
  assert.equal(a.lists.length,1);assert.equal(b.lists[1].name,"Otra compra");assert.equal(c.lists[1].name,"Mercado");
  assert.deepEqual(removeList(c,"l").lists.map(x=>x.id),["m"]);
  assert.throws(()=>addList(a,"l","Duplicada"));assert.throws(()=>removeList(a,"missing"));
});
test("artículos separados y edición de cantidades literales",()=>{
  const a=stocked(),b=addItem(a,"l",item("b")),c=editItem(b,"l","a",item("a",{quantity:"0.250"}));
  assert.equal(a.lists[0].items.length,1);assert.equal(b.lists[0].items[0].quantity,"1.50");
  assert.equal(c.lists[0].items[0].quantity,"0.250");
  assert.deepEqual(removeItem(c,"l","b").lists[0].items.map(x=>x.id),["a"]);
  assert.throws(()=>editItem(b,"l","a",item("c")));
});
test("cantidades y unidades siguen las reglas de Pantry",()=>{
  assert.equal(validateItem(item("a",{quantity:null,unit:null})).quantity,null);
  for(const quantity of ["0","-1","1e3","1–2","1,5",1])assert.throws(()=>validateItem(item("a",{quantity})));
  assert.throws(()=>validateItem(item("a",{quantity:null})));
  assert.throws(()=>validateItem(item("a",{unit:null})));
});
test("identidades globales y límites",()=>{
  const a=addList(stocked(),"m","Otra");
  assert.throws(()=>addItem(a,"m",item("a")));assert.throws(()=>addItem(a,"m",item("l")));
  assert.throws(()=>validateItem(item("a".repeat(72))));
  assert.throws(()=>validateShopping({schema_version:"9",lists:[]}));
  assert.throws(()=>validateShopping({...emptyShopping(),lists:Array.from({length:MAX_LISTS+1},(_,i)=>({id:"l"+i,name:"Lista",items:[]}))}));
  assert.throws(()=>validateShopping({...emptyShopping(),lists:[{id:"l",name:"Lista",items:Array(MAX_ITEMS+1).fill(item())}]}));
});
test("procedencia literal preservada, copiada y no editable",()=>{
  const a=addItem(initial(),"l",item("a",{provenance:origin,quantity:null,unit:null}));
  const b=editItem(a,"l","a",item("a",{provenance:origin,quantity:"1",unit:"taza"}));
  assert.equal(b.lists[0].items[0].provenance.raw,origin.raw);
  assert.throws(()=>editItem(a,"l","a",item()));
  assert.throws(()=>validateItem(item("a",{provenance:{...origin,position:-1}})));
  assert.throws(()=>validateItem(item("a",{provenance:{...origin,source_location:{start_line:2,end_line:1}}})));
  const c=validateShopping(a);c.lists[0].items[0].provenance.source_location.start_line=99;
  assert.equal(a.lists[0].items[0].provenance.source_location.start_line,10);
});
test("compra reversible e independiente de transferencia",()=>{
  const a=stocked(),b=markPurchased(a,"l","a",true),c=markPurchased(b,"l","a",false);
  assert.equal(a.lists[0].items[0].purchased,false);assert.equal(b.lists[0].items[0].transfer,null);
  assert.equal(c.lists[0].items[0].purchased,false);
  assert.throws(()=>markPurchased(a,"l","a",1));
});
test("filtros acumulables, Unicode y orden",()=>{
  const a=addItem(addItem(stocked(),"l",item("b",{name:"Cafe\u0301",category:"Bebidas",purchased:true})),"l",item("c",{name:"Café",category:"Bebidas"}));
  assert.deepEqual(filterItems(a,"l",{name:"CAFÉ",category:"bebidas"}).map(x=>x.id),["b","c"]);
  assert.deepEqual(filterItems(a,"l",{purchased:true,transfer:"none"}).map(x=>x.id),["b"]);
  assert.deepEqual(filterItems(a,"l",{name:"nada"}),[]);
  assert.throws(()=>filterItems(a,"l",{transfer:"unknown"}));
});
test("intención de transferencia solo para artículos comprados y destino estable",()=>{
  const a=stocked(),b=markPurchased(a,"l","a",true);
  assert.throws(()=>prepareTransfer(a,"l","a",target()));
  assert.throws(()=>prepareTransfer(b,"l","a",target({id:"other"})));
  const c=prepareTransfer(b,"l","a",target());
  assert.equal(c.lists[0].items[0].transfer.state,"pending");
  assert.equal(b.lists[0].items[0].transfer,null);
  assert.throws(()=>prepareTransfer(c,"l","a",target()));
  assert.throws(()=>addItem(initial(),"l",c.lists[0].items[0]));
});
test("registro de finalización exige intención y coincidencia íntegra",()=>{
  const a=markPurchased(stocked(),"l","a",true),b=prepareTransfer(a,"l","a",target());
  assert.throws(()=>recordTransferCompleted(a,"l","a",target()));
  assert.throws(()=>recordTransferCompleted(b,"l","a",target({quantity:"2"})));
  const c=recordTransferCompleted(b,"l","a",target());
  assert.equal(c.lists[0].items[0].transfer.state,"completed");
  assert.equal(b.lists[0].items[0].transfer.state,"pending");
  assert.throws(()=>recordTransferCompleted(c,"l","a",target()));
  assert.deepEqual(filterItems(c,"l",{transfer:"completed"}).map(x=>x.id),["a"]);
});
test("registros de transferencia protegidos frente a borrado, edición y desmarcado",()=>{
  const a=prepareTransfer(markPurchased(stocked(),"l","a",true),"l","a",target());
  for(const data of [a,recordTransferCompleted(a,"l","a",target())]){
    assert.throws(()=>removeItem(data,"l","a"));assert.throws(()=>removeList(data,"l"));
    assert.throws(()=>editItem(data,"l","a",item()));assert.throws(()=>markPurchased(data,"l","a",false));
  }
});
