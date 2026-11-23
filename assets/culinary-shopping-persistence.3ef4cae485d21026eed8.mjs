/* Persistencia local explícita; el adaptador recibe Storage y no usa DOM ni red. */
import {SCHEMA_VERSION,emptyShopping,validateShopping} from "./culinary-shopping-model.3ef4cae485d21026eed8.mjs";
export const STORAGE_KEY="novacoquinaria.culinary-shopping";
export const MAX_JSON_LENGTH=12000000;
export class ShoppingStorageError extends Error {
  constructor(code,message){super(message);this.name="ShoppingStorageError";this.code=code;}
}
const fail=(code,message)=>{throw new ShoppingStorageError(code,message);};
export function parseBackup(raw){
  if(typeof raw!=="string"||raw.length>MAX_JSON_LENGTH)fail("invalid","Copia inválida o demasiado grande.");
  let value;
  try{value=JSON.parse(raw);}catch{fail("invalid","JSON no válido.");}
  if(value&&typeof value==="object"&&Object.hasOwn(value,"schema_version")&&value.schema_version!==SCHEMA_VERSION)
    fail("version","Versión de documento de compras no admitida.");
  try{return validateShopping(value);}catch{fail("invalid","Documento de compras incompatible con el esquema.");}
}
export function serializeBackup(data){
  const raw=JSON.stringify(validateShopping(data),null,2);
  if(raw.length>MAX_JSON_LENGTH)fail("invalid","Documento de compras demasiado grande.");
  return raw;
}
export function createShoppingPersistence(getStorage){
  let storage, baseline, lastValid=null, ready=false, dirtyExternal=false;
  function access(){
    try{storage=getStorage();if(!storage)throw new Error();return storage;}
    catch{fail("blocked","Almacenamiento local no disponible.");}
  }
  function read(){
    try{return access().getItem(STORAGE_KEY);}
    catch(error){if(error instanceof ShoppingStorageError)throw error;fail("read","No se pudo leer el documento de compras local.");}
  }
  function load(){
    ready=false;
    const raw=read();
    const data=raw===null?emptyShopping():parseBackup(raw);
    baseline=raw;lastValid=data;ready=true;dirtyExternal=false;
    return {status:raw===null?"absent":"loaded",data:validateShopping(data)};
  }
  function snapshot(){return lastValid===null?null:validateShopping(lastValid);}
  function save(data){
    if(!ready)fail("not_ready","Carga primero un documento de compras válido.");
    const raw=serializeBackup(data);
    if(dirtyExternal||read()!==baseline){dirtyExternal=true;fail("conflict","El documento de compras cambió en otra pestaña. Recarga antes de guardar.");}
    try{storage.setItem(STORAGE_KEY,raw);}
    catch(error){
      if(error?.name==="QuotaExceededError")fail("quota","Espacio local insuficiente; no se guardaron los cambios.");
      fail("write","No se pudo guardar el documento de compras.");
    }
    baseline=raw;lastValid=parseBackup(raw);
    return snapshot();
  }
  function observeStorageEvent(event){
    if(event&&(event.key===STORAGE_KEY||event.key===null)&&
        (event.storageArea==null||event.storageArea===storage)){
      if(event.key===null||event.newValue!==baseline)dirtyExternal=true;
    }
    return dirtyExternal;
  }
  function previewImport(raw){
    const data=parseBackup(raw);
    return Object.freeze({listCount:data.lists.length,itemCount:data.lists.reduce((n,l)=>n+l.items.length,0),raw:serializeBackup(data)});
  }
  function confirmImport(preview,confirmed){
    if(confirmed!==true)return {status:"cancelled",data:snapshot()};
    const data=parseBackup(preview?.raw);
    if(preview.listCount!==data.lists.length||preview.itemCount!==data.lists.reduce((n,l)=>n+l.items.length,0))fail("invalid","Previsualización incompatible.");
    // La copia no puede descartar ni alterar registros de transferencia vigentes.
    const records=new Map(data.lists.flatMap(l=>l.items.filter(i=>i.transfer!==null).map(i=>[i.id,i.transfer])));
    for(const list of lastValid?.lists??[])for(const item of list.items){
      if(item.transfer!==null&&JSON.stringify(records.get(item.id))!==JSON.stringify(item.transfer))
        fail("transfer_history","La copia no conserva los registros de transferencia actuales; no se ha sustituido el documento.");
    }
    return {status:"imported",data:save(data)};
  }
  function exportLastValid(){
    if(lastValid===null)fail("not_ready","No hay una copia válida disponible.");
    return serializeBackup(lastValid);
  }
  return {load,snapshot,save,observeStorageEvent,previewImport,confirmImport,exportLastValid};
}
