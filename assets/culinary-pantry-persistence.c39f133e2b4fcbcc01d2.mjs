/* Persistencia local explícita; el adaptador recibe Storage y no usa DOM ni red. */
import {SCHEMA_VERSION,emptyPantry,validatePantry} from "./culinary-pantry-model.c39f133e2b4fcbcc01d2.mjs";
export const STORAGE_KEY="novacoquinaria.culinary-pantry";
export const MAX_JSON_LENGTH=16000000;
export class PantryStorageError extends Error {
  constructor(code,message){super(message);this.name="PantryStorageError";this.code=code;}
}
const fail=(code,message)=>{throw new PantryStorageError(code,message);};
export function parseBackup(raw){
  if(typeof raw!=="string"||raw.length>MAX_JSON_LENGTH)fail("invalid","Copia inválida o demasiado grande.");
  let value;
  try{value=JSON.parse(raw);}catch{fail("invalid","JSON no válido.");}
  if(value&&typeof value==="object"&&Object.hasOwn(value,"schema_version")&&value.schema_version!==SCHEMA_VERSION)
    fail("version","Versión de inventario no admitida.");
  try{return validatePantry(value);}catch{fail("invalid","Inventario incompatible con el esquema.");}
}
export function serializeBackup(data){
  const raw=JSON.stringify(validatePantry(data),null,2);
  if(raw.length>MAX_JSON_LENGTH)fail("invalid","Inventario demasiado grande.");
  return raw;
}
export function createPantryPersistence(getStorage){
  let storage, baseline, lastValid=null, ready=false, dirtyExternal=false;
  function access(){
    try{storage=getStorage();if(!storage)throw new Error();return storage;}
    catch{fail("blocked","Almacenamiento local no disponible.");}
  }
  function read(){
    try{return access().getItem(STORAGE_KEY);}
    catch(error){if(error instanceof PantryStorageError)throw error;fail("read","No se pudo leer el inventario local.");}
  }
  function load(){
    ready=false;
    const raw=read();
    const data=raw===null?emptyPantry():parseBackup(raw);
    baseline=raw;lastValid=data;ready=true;dirtyExternal=false;
    return {status:raw===null?"absent":"loaded",data:validatePantry(data)};
  }
  function snapshot(){return lastValid===null?null:validatePantry(lastValid);}
  function save(data){
    if(!ready)fail("not_ready","Carga primero un inventario válido.");
    const raw=serializeBackup(data);
    if(dirtyExternal||read()!==baseline){dirtyExternal=true;fail("conflict","El inventario cambió en otra pestaña. Recarga antes de guardar.");}
    try{storage.setItem(STORAGE_KEY,raw);}
    catch(error){
      if(error?.name==="QuotaExceededError")fail("quota","Espacio local insuficiente; no se guardaron los cambios.");
      fail("write","No se pudo guardar el inventario.");
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
    return Object.freeze({count:data.entries.length,raw:serializeBackup(data)});
  }
  function confirmImport(preview,confirmed){
    if(confirmed!==true)return {status:"cancelled",data:snapshot()};
    const data=parseBackup(preview?.raw);
    if(preview.count!==data.entries.length)fail("invalid","Previsualización incompatible.");
    return {status:"imported",data:save(data)};
  }
  function exportLastValid(){
    if(lastValid===null)fail("not_ready","No hay una copia válida disponible.");
    return serializeBackup(lastValid);
  }
  return {load,snapshot,save,observeStorageEvent,previewImport,confirmImport,exportLastValid};
}
