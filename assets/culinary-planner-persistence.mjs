/* Adaptador local y versionado del plan; sin DOM, red ni claves compartidas. */
import {SCHEMA_VERSION,emptyPlanner,validatePlanner} from "./culinary-planner-model.mjs";
export const STORAGE_KEY="novacoquinaria.culinary-planner";
export const MAX_JSON_LENGTH=12000000;
export class PlannerStorageError extends Error{
  constructor(code,message){super(message);this.name="PlannerStorageError";this.code=code;}
}
const fail=(code,message)=>{throw new PlannerStorageError(code,message);};
export function parseBackup(raw){
  if(typeof raw!=="string"||raw.length>MAX_JSON_LENGTH)fail("invalid","Copia inválida o demasiado grande.");
  let value;
  try{value=JSON.parse(raw);}catch{fail("invalid","JSON no válido.");}
  if(value!==null&&typeof value==="object"&&Object.hasOwn(value,"schema_version")&&value.schema_version!==SCHEMA_VERSION)
    fail("version","Versión del plan no admitida.");
  try{return validatePlanner(value);}catch{fail("invalid","Plan incompatible con el esquema.");}
}
export function serializeBackup(data){
  let raw;
  try{raw=JSON.stringify(validatePlanner(data),null,2);}catch{fail("invalid","Plan incompatible con el esquema.");}
  if(raw.length>MAX_JSON_LENGTH)fail("invalid","Copia del plan demasiado grande.");
  return raw;
}
export function createPlannerPersistence(getStorage){
  let storage=null,baseline=null,lastValid=null,ready=false,external=false;
  const access=()=>{
    try{storage=getStorage();if(!storage)throw Error();return storage;}
    catch{fail("blocked","Almacenamiento local no disponible.");}
  };
  function read(){
    try{return access().getItem(STORAGE_KEY);}
    catch(e){if(e instanceof PlannerStorageError)throw e;fail("read","No se pudo leer el plan.");}
  }
  function snapshot(){return lastValid===null?null:validatePlanner(lastValid);}
  function load(){
    ready=false;
    const raw=read(),data=raw===null?emptyPlanner():parseBackup(raw);
    baseline=raw;lastValid=data;external=false;ready=true;
    return {status:raw===null?"absent":"loaded",data:snapshot()};
  }
  function save(data){
    if(!ready)fail("not_ready","Carga primero un plan válido.");
    const raw=serializeBackup(data);
    if(external||read()!==baseline){external=true;fail("conflict","El plan cambió en otra pestaña. Recarga antes de guardar.");}
    try{storage.setItem(STORAGE_KEY,raw);}
    catch(e){
      if(e?.name==="QuotaExceededError")fail("quota","Espacio local insuficiente; no se guardaron los cambios.");
      fail("write","No se pudo guardar el plan.");
    }
    baseline=raw;lastValid=parseBackup(raw);
    return snapshot();
  }
  function observeStorageEvent(event){
    if(event&&(event.key===STORAGE_KEY||event.key===null)&&
      (event.storageArea==null||event.storageArea===storage)){
      if(event.key===null||event.newValue!==baseline)external=true;
    }
    return external;
  }
  let pendingPreview=null;
  function previewImport(raw){
    const data=parseBackup(raw),canonical=serializeBackup(data);
    pendingPreview=Object.freeze({count:data.entries.length,raw:canonical});
    return pendingPreview;
  }
  function confirmImport(preview,confirmed){
    if(confirmed!==true){pendingPreview=null;return {status:"cancelled",data:snapshot()};}
    if(!ready)fail("not_ready","Carga primero un plan válido.");
    if(preview!==pendingPreview||preview===null)fail("invalid","Previsualización de importación desconocida.");
    const data=parseBackup(preview.raw);
    if(preview.count!==data.entries.length)fail("invalid","Recuento incompatible.");
    // La sustitución explícita nunca modifica Pantry o Shopping.
    const result=save(data);pendingPreview=null;
    return {status:"imported",data:result};
  }
  function exportLastValid(){
    if(lastValid===null)fail("not_ready","No existe copia válida disponible.");
    return serializeBackup(lastValid);
  }
  return {load,snapshot,save,observeStorageEvent,previewImport,confirmImport,exportLastValid};
}
