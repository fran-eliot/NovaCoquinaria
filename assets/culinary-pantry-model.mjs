/* Inventario declarado; sin DOM, almacenamiento, red ni semántica canónica. */
export const SCHEMA_VERSION="0.1.0";
export const MAX_ENTRIES=2000;
export const LOCATIONS=Object.freeze(["pantry","fridge","freezer","other"]);
export const DATE_TYPES=Object.freeze(["expiry","best_before"]);
const fields=["id","name","quantity","unit","category","location","date_type","date","notes"];
const fail=message=>{throw new Error(message);};
function require(condition,message){if(!condition)fail(message);}
function exactKeys(obj,keys){
  return obj!==null && typeof obj==="object" && !Array.isArray(obj) &&
    Object.keys(obj).length===keys.length && keys.every(k=>Object.hasOwn(obj,k));
}
function string(value,max,nullable=false,multiline=false){
  if(nullable&&value===null)return;
  require(typeof value==="string" && value.length>0 && value.length<=max &&
    value.trim()===value && !(multiline?/[\u0000-\u0008\u000b-\u001f\u007f]/u:/[\u0000-\u001f\u007f]/u).test(value),"Texto inválido");
}
export function validDate(value){
  if(typeof value!=="string"||!/^\d{4}-\d{2}-\d{2}$/.test(value))return false;
  const [year,month,day]=value.split("-").map(Number);
  const leap=year%4===0&&(year%100!==0||year%400===0);
  return year>=1&&month>=1&&month<=12&&day>=1&&day<=[31,leap?29:28,31,30,31,30,31,31,30,31,30,31][month-1];
}
export function dateRelation(value,today){
  require(validDate(today),"Fecha de referencia inválida");
  if(value===null)return "undated";
  require(validDate(value),"Fecha inválida");
  return value<today?"past":value===today?"today":"future";
}
export function validateEntry(entry){
  require(exactKeys(entry,fields),"Campos de entrada inválidos");
  require(typeof entry.id==="string"&&/^[A-Za-z0-9_-]{1,80}$/.test(entry.id),"Identificador inválido");
  string(entry.name,160);string(entry.category,80,true);string(entry.notes,1000,true,true);
  require(LOCATIONS.includes(entry.location),"Ubicación inválida");
  if(entry.quantity===null)require(entry.unit===null,"Unidad sin cantidad");
  else{
    require(typeof entry.quantity==="string"&&/^(?:0|[1-9]\d{0,8})(?:\.\d{1,6})?$/.test(entry.quantity)&&/[1-9]/.test(entry.quantity),"Cantidad decimal positiva inválida");
    string(entry.unit,40);
  }
  require((entry.date===null&&entry.date_type===null)||
    (validDate(entry.date)&&DATE_TYPES.includes(entry.date_type)),"Fecha y tipo incoherentes");
  return {...entry};
}
export function emptyPantry(){return {schema_version:SCHEMA_VERSION,entries:[]};}
export function validatePantry(data){
  require(exactKeys(data,["schema_version","entries"])&&data.schema_version===SCHEMA_VERSION,"Esquema no admitido");
  require(Array.isArray(data.entries)&&data.entries.length<=MAX_ENTRIES,"Inventario inválido o demasiado grande");
  const ids=new Set();
  const entries=data.entries.map(entry=>{
    const copy=validateEntry(entry);
    require(!ids.has(copy.id),"ID duplicado");ids.add(copy.id);return copy;
  });
  return {schema_version:SCHEMA_VERSION,entries};
}
export function addEntry(data,entry){
  const next=validatePantry(data);next.entries.push(validateEntry(entry));return validatePantry(next);
}
export function editEntry(data,id,entry){
  const next=validatePantry(data),index=next.entries.findIndex(e=>e.id===id);
  require(index>=0&&entry?.id===id,"Entrada desconocida o identidad modificada");
  next.entries[index]=validateEntry(entry);return next;
}
export function removeEntry(data,id){
  const next=validatePantry(data),index=next.entries.findIndex(e=>e.id===id);
  require(index>=0,"Entrada desconocida");
  next.entries.splice(index,1);return next;
}
const key=value=>value.normalize("NFC").toLowerCase().normalize("NFC").trim();
export function filterEntries(data,{name="",category=null,location=null,relation=null,today=null}={}){
  const next=validatePantry(data);
  require(typeof name==="string"&&(category===null||typeof category==="string")&&
    (location===null||LOCATIONS.includes(location))&&
    (relation===null||["past","today","future","undated"].includes(relation)),"Filtro inválido");
  if(relation!==null)require(validDate(today),"Fecha de referencia inválida");
  return next.entries.filter(e=>key(e.name).includes(key(name))&&
    (category===null||key(e.category??"")===key(category))&&
    (location===null||e.location===location)&&
    (relation===null||dateRelation(e.date,today)===relation));
}
export function selectedMentions(data,ids){
  const next=validatePantry(data);
  require(Array.isArray(ids)&&ids.length>0&&new Set(ids).size===ids.length,"Selección explícita inválida");
  const byId=new Map(next.entries.map(e=>[e.id,e]));
  const names=[];
  for(const id of ids){
    require(byId.has(id),"Entrada seleccionada desconocida");
    const name=byId.get(id).name;
    require(/[\p{L}\p{N}]/u.test(name),"Mención sin términos");
    if(!names.some(n=>key(n)===key(name)))names.push(name);
  }
  return names;
}
