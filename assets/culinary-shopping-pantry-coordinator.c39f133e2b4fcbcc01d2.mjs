/* Coordinación explícita de una transferencia. No es una transacción entre claves. */
import {prepareTransfer,recordTransferCompleted,validateShopping} from "./culinary-shopping-model.c39f133e2b4fcbcc01d2.mjs";
import {validateEntry,addEntry} from "./culinary-pantry-model.c39f133e2b4fcbcc01d2.mjs";
const fail=message=>{throw Error(message);};
function getItem(data,listId,itemId){
  const item=data.lists.find(l=>l.id===listId)?.items.find(i=>i.id===itemId);
  if(!item)fail("Artículo desconocido.");return item;
}
const equal=(a,b)=>a&&b&&Object.keys(b).every(k=>a[k]===b[k]);
function checkCurrent(store,expected){
  const actual=store.load().data;
  if(JSON.stringify(actual)!==JSON.stringify(expected))fail("Las compras cambiaron. Recarga y revisa antes de continuar.");
  return actual;
}
function finish(shopping,pantry,data,listId,itemId,entry){
  const current=pantry.load().data.entries.find(e=>e.id===entry.id);
  if(!equal(current,entry))fail("No se acredita el destino exacto en la despensa. No se repetirá la escritura automáticamente.");
  checkCurrent(shopping,data);
  return shopping.save(recordTransferCompleted(data,listId,itemId,current));
}
/* Solo una operación nueva y confirmada puede crear un lote. */
export function transferPurchased({shopping,pantry,expected,listId,itemId,entry,confirmed}){
  if(confirmed!==true)return {status:"cancelled"};
  const data=checkCurrent(shopping,validateShopping(expected)),target=validateEntry(entry);
  const intent=prepareTransfer(data,listId,itemId,target);
  const before=pantry.load().data;
  if(before.entries.some(e=>e.id===target.id))fail("Ya existe el identificador de destino. Revisa la despensa; no se crea otro lote.");
  const next=addEntry(before,target);
  const pending=shopping.save(intent);
  // Si falla a partir de aquí, se conserva la intención. No se compensa ni se repite.
  checkCurrent(shopping,pending);
  pantry.save(next);
  return {status:"completed",data:finish(shopping,pantry,pending,listId,itemId,target)};
}
/* Recuperación conservadora: una intención existente jamás vuelve a crear un lote.
   La ausencia puede significar que el lote se consumió, editó o eliminó. */
export function recoverTransfer({shopping,pantry,expected,listId,itemId,confirmed}){
  if(confirmed!==true)return {status:"cancelled"};
  const data=checkCurrent(shopping,validateShopping(expected)),item=getItem(data,listId,itemId);
  if(item.transfer?.state!=="pending")fail("No hay una transferencia pendiente.");
  return {status:"completed",data:finish(shopping,pantry,data,listId,itemId,item.transfer.entry)};
}
