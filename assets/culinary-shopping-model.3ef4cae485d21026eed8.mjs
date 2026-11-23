/* Listas declaradas: núcleo puro, sin almacenamiento, DOM, red ni inferencia. */
import {validateEntry} from "./culinary-pantry-model.3ef4cae485d21026eed8.mjs";
export const SCHEMA_VERSION="0.1.0";
export const MAX_LISTS=100, MAX_ITEMS=2000;
const require=(ok,message)=>{if(!ok)throw Error(message);};
const keys=(o,k)=>o!==null&&typeof o==="object"&&!Array.isArray(o)&&Object.keys(o).length===k.length&&k.every(x=>Object.hasOwn(o,x));
const id=v=>typeof v==="string"&&/^[A-Za-z0-9_-]{1,80}$/.test(v);
const name=v=>typeof v==="string"&&v.length>0&&v.length<=160&&v.trim()===v&&!/[\u0000-\u001f\u007f]/u.test(v);
function provenance(p){
  if(p===null)return null;
  require(keys(p,["recipe_id","position","source_location","raw","source_commit"])&&id(p.recipe_id)&&
    Number.isSafeInteger(p.position)&&p.position>=0&&typeof p.raw==="string"&&p.raw.trim().length>0&&p.raw.length<=8000&&
    typeof p.source_commit==="string"&&/^[a-f0-9]{40}$/.test(p.source_commit),"Procedencia de receta inválida");
  const l=p.source_location;
  require(keys(l,["start_line","end_line"])&&Number.isSafeInteger(l.start_line)&&Number.isSafeInteger(l.end_line)&&l.start_line>=1&&l.end_line>=l.start_line,"Localizador inválido");
  return {...p,source_location:{...l}};
}
export function validateItem(item){
  require(keys(item,["id","name","quantity","unit","category","notes","purchased","provenance","transfer"]),"Campos de artículo inválidos");
  const {id:identity,name,quantity,unit,category,notes}=item;
  validateEntry({id:identity,name,quantity,unit,category,notes,location:"other",date_type:null,date:null});
  require(typeof item.purchased==="boolean","Estado de compra inválido");
  let transfer=null;
  if(item.transfer!==null){
    const t=item.transfer;
    require(keys(t,["state","entry"])&&["pending","completed"].includes(t.state)&&item.purchased,"Estado de transferencia inválido");
    const entry=validateEntry(t.entry);
    require(entry.id==="shopping-"+identity && identity.length<=71,"Identidad de destino incoherente");
    transfer={state:t.state,entry};
  }
  require(identity.length<=71,"Identificador de artículo demasiado largo");
  return {...item,provenance:provenance(item.provenance),transfer};
}
export function emptyShopping(){return {schema_version:SCHEMA_VERSION,lists:[]};}
export function validateShopping(data){
  require(keys(data,["schema_version","lists"])&&data.schema_version===SCHEMA_VERSION&&Array.isArray(data.lists)&&data.lists.length<=MAX_LISTS,"Esquema de compras inválido");
  const ids=new Set();let count=0;
  const unique=v=>{require(id(v)&&!ids.has(v),"ID inválido o duplicado");ids.add(v);};
  const lists=Array.from(data.lists,list=>{
    require(keys(list,["id","name","items"])&&name(list.name)&&Array.isArray(list.items),"Lista inválida");
    unique(list.id);count+=list.items.length;require(count<=MAX_ITEMS,"Demasiados artículos");
    return {id:list.id,name:list.name,items:Array.from(list.items,item=>{const copy=validateItem(item);unique(copy.id);return copy;})};
  });
  return {schema_version:SCHEMA_VERSION,lists};
}
function find(data,listId){const list=data.lists.find(l=>l.id===listId);require(list,"Lista desconocida");return list;}
function locate(list,itemId){const i=list.items.findIndex(x=>x.id===itemId);require(i>=0,"Artículo desconocido");return i;}
export function addList(data,listId,title){
  const next=validateShopping(data);next.lists.push({id:listId,name:title,items:[]});return validateShopping(next);
}
export function renameList(data,listId,title){
  const next=validateShopping(data);find(next,listId).name=title;return validateShopping(next);
}
export function removeList(data,listId){
  const next=validateShopping(data),list=find(next,listId);
  require(!list.items.some(x=>x.transfer!==null),"La lista contiene un registro de transferencia; consérvalo");
  next.lists=next.lists.filter(l=>l.id!==listId);return next;
}
export function addItem(data,listId,item){
  const next=validateShopping(data);require(item?.transfer===null,"No se admiten transferencias al crear artículos");
  find(next,listId).items.push(validateItem(item));return validateShopping(next);
}
export function editItem(data,listId,itemId,item){
  const next=validateShopping(data),list=find(next,listId),i=locate(list,itemId),old=list.items[i];
  require(old.transfer===null&&item?.transfer===null&&item.id===itemId,"Artículo bloqueado o identidad modificada");
  require(JSON.stringify(provenance(item.provenance))===JSON.stringify(old.provenance),"No se permite modificar la procedencia histórica");
  list.items[i]=validateItem(item);return next;
}
export function markPurchased(data,listId,itemId,purchased){
  const next=validateShopping(data),list=find(next,listId),i=locate(list,itemId);
  require(typeof purchased==="boolean"&&list.items[i].transfer===null,"Estado inválido o artículo transferido");
  list.items[i].purchased=purchased;return next;
}
export function removeItem(data,listId,itemId){
  const next=validateShopping(data),list=find(next,listId),i=locate(list,itemId);
  require(list.items[i].transfer===null,"Conserva el registro de transferencia");
  list.items.splice(i,1);return next;
}
/* Solo registra la intención revisada; no escribe en Pantry. */
export function prepareTransfer(data,listId,itemId,entry){
  const next=validateShopping(data),list=find(next,listId),i=locate(list,itemId),item=list.items[i];
  require(item.purchased&&item.transfer===null,"El artículo no está disponible para transferir");
  item.transfer={state:"pending",entry:validateEntry(entry)};return validateShopping(next);
}
/* El coordinador de integración deberá acreditar la escritura antes de llamar. */
export function recordTransferCompleted(data,listId,itemId,verifiedEntry){
  const next=validateShopping(data),list=find(next,listId),i=locate(list,itemId),item=list.items[i];
  require(item.transfer?.state==="pending","No existe intención pendiente");
  const verified=validateEntry(verifiedEntry);
  require(Object.keys(verified).every(k=>verified[k]===item.transfer.entry[k]),"Destino distinto de la intención");
  item.transfer.state="completed";return next;
}
const key=v=>v.normalize("NFC").toLowerCase().normalize("NFC").trim();
export function filterItems(data,listId,{name="",category=null,purchased=null,transfer=null}={}){
  const list=find(validateShopping(data),listId);
  require(typeof name==="string"&&(category===null||typeof category==="string")&&(purchased===null||typeof purchased==="boolean")&&
    (transfer===null||["none","pending","completed"].includes(transfer)),"Filtro inválido");
  return list.items.filter(i=>key(i.name).includes(key(name))&&(category===null||key(i.category??"")===key(category))&&
    (purchased===null||i.purchased===purchased)&&(transfer===null||(i.transfer?.state??"none")===transfer));
}
