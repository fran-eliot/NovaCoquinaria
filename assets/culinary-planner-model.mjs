/* Planificación civil declarada; núcleo puro sin DOM, red ni persistencia. */
export const SCHEMA_VERSION="0.1.0";
export const MAX_ENTRIES=2000;
export const MEALS=Object.freeze(["breakfast","lunch","dinner","other"]);
const fields=["id","date","meal","title","notes","source"];
const maxDate="9999-12-31";
const fail=message=>{throw new Error(message);};
const require=(ok,message)=>{if(!ok)fail(message);};
const exactKeys=(obj,keys)=>obj!==null&&typeof obj==="object"&&!Array.isArray(obj)&&
  Object.keys(obj).length===keys.length&&keys.every(key=>Object.hasOwn(obj,key));
const validId=id=>typeof id==="string"&&/^[A-Za-z0-9_-]{1,80}$/.test(id);
const validText=(text,max,multiline=false)=>typeof text==="string"&&text.length>0&&
  text.length<=max&&text.trim()===text&&
  !(multiline?/[\u0000-\u0008\u000b-\u001f\u007f]/u:/[\u0000-\u001f\u007f]/u).test(text);
const leap=y=>y%4===0&&(y%100!==0||y%400===0);
const monthDays=(y,m)=>[31,leap(y)?29:28,31,30,31,30,31,31,30,31,30,31][m-1];
export function validCivilDate(value){
  if(typeof value!=="string"||!/^\d{4}-\d{2}-\d{2}$/.test(value))return false;
  const [y,m,d]=value.split("-").map(Number);
  return y>=1&&y<=9999&&m>=1&&m<=12&&d>=1&&d<=monthDays(y,m);
}
function ordinal(date){
  require(validCivilDate(date),"Fecha civil inválida");
  const [y,m,d]=date.split("-").map(Number),prev=y-1;
  let total=365*prev+Math.floor(prev/4)-Math.floor(prev/100)+Math.floor(prev/400)+d;
  for(let i=1;i<m;i++)total+=monthDays(y,i);
  return total;
}
const MAX_DAY=365*9999+Math.floor(9998/4)-Math.floor(9998/100)+Math.floor(9998/400);
function fromOrdinal(day){
  require(Number.isSafeInteger(day)&&day>=1&&day<=MAX_DAY,"Fecha fuera del calendario admitido");
  let low=1,high=9999;
  while(low<high){
    const mid=Math.ceil((low+high)/2),before=mid-1;
    const start=365*before+Math.floor(before/4)-Math.floor(before/100)+Math.floor(before/400)+1;
    if(start<=day)low=mid;else high=mid-1;
  }
  const y=low,prev=y-1;
  let rest=day-(365*prev+Math.floor(prev/4)-Math.floor(prev/100)+Math.floor(prev/400));
  let m=1;
  while(rest>monthDays(y,m)){rest-=monthDays(y,m);m++;}
  return String(y).padStart(4,"0")+"-"+String(m).padStart(2,"0")+"-"+String(rest).padStart(2,"0");
}
export function shiftCivilDate(date,days){
  require(Number.isSafeInteger(days)&&Math.abs(days)<=MAX_DAY,"Desplazamiento inválido");
  return fromOrdinal(ordinal(date)+days);
}
export function weekStart(date){
  const day=ordinal(date);
  return fromOrdinal(day-(day-1)%7); // 0001-01-01 es lunes en el calendario gregoriano proléptico.
}
export function weekDates(date){
  const start=ordinal(weekStart(date));
  require(start+6<=MAX_DAY,"La semana excede el calendario admitido");
  return Array.from({length:7},(_,i)=>fromOrdinal(start+i));
}
function validateSource(source){
  require(source!==null&&typeof source==="object"&&!Array.isArray(source),"Origen inválido");
  if(exactKeys(source,["type"])&&source.type==="free_text")return {type:"free_text"};
  require(exactKeys(source,["type","recipe_id","source_commit","source_path"])&&source.type==="recipe",
    "Contrato de origen inválido");
  require(validId(source.recipe_id)&&/^[a-f0-9]{40}$/.test(source.source_commit)&&
    typeof source.source_path==="string"&&source.source_path.length>0&&source.source_path.length<=500&&
    /^[0-9]{2}_[^?#\\\u0000-\u001f]+\/[^?#\\\u0000-\u001f]+\.md$/u.test(source.source_path)&&
    !source.source_path.split("/").includes("..")&&!source.source_path.split("/").includes(".")&&
    !/%(?:2e|2f|5c)/iu.test(source.source_path),
    "Referencia documental inválida");
  return {...source};
}
export function validatePlanEntry(entry){
  require(exactKeys(entry,fields),"Campos de planificación inválidos");
  require(validId(entry.id),"ID de planificación inválido");
  require(validCivilDate(entry.date),"Fecha de planificación inválida");
  require(MEALS.includes(entry.meal),"Momento de comida inválido");
  require(validText(entry.title,160),"Título inválido");
  require(entry.notes===null||validText(entry.notes,1000,true),"Notas inválidas");
  const source=validateSource(entry.source);
  return {...entry,source};
}
export function emptyPlanner(){return {schema_version:SCHEMA_VERSION,entries:[]};}
export function validatePlanner(data){
  require(exactKeys(data,["schema_version","entries"])&&data.schema_version===SCHEMA_VERSION,
    "Esquema de planificación incompatible");
  require(Array.isArray(data.entries)&&data.entries.length<=MAX_ENTRIES,"Plan demasiado grande o inválido");
  const ids=new Set();
  const entries=data.entries.map(entry=>{
    const copy=validatePlanEntry(entry);
    require(!ids.has(copy.id),"ID de entrada duplicado");
    ids.add(copy.id);return copy;
  });
  return {schema_version:SCHEMA_VERSION,entries};
}
export function addPlanEntry(data,entry){
  const next=validatePlanner(data);next.entries.push(validatePlanEntry(entry));return validatePlanner(next);
}
export function editPlanEntry(data,id,updated){
  const next=validatePlanner(data),index=next.entries.findIndex(entry=>entry.id===id);
  require(index>=0&&updated?.id===id,"Entrada desconocida o identidad modificada");
  const candidate=validatePlanEntry(updated),original=next.entries[index];
  require(JSON.stringify(candidate.source)===JSON.stringify(original.source),
    "La procedencia de una entrada no puede cambiarse; crea otra entrada");
  next.entries[index]=candidate;return next;
}
export function removePlanEntry(data,id){
  const next=validatePlanner(data),index=next.entries.findIndex(entry=>entry.id===id);
  require(index>=0,"Entrada desconocida");
  next.entries.splice(index,1);return next;
}
const normalize=value=>value.normalize("NFC").toLocaleLowerCase("es").normalize("NFC");
export function filterPlanEntries(data,{start=null,end=null,meal=null,title=""}={}){
  const next=validatePlanner(data);
  require(start===null||validCivilDate(start),"Inicio inválido");
  require(end===null||validCivilDate(end),"Fin inválido");
  require(start===null||end===null||start<=end,"Intervalo invertido");
  require(meal===null||MEALS.includes(meal),"Momento inválido");
  require(typeof title==="string"&&title.length<=160,"Filtro de título inválido");
  const query=normalize(title.trim());
  return next.entries.filter(entry=>(start===null||entry.date>=start)&&
    (end===null||entry.date<=end)&&(meal===null||entry.meal===meal)&&
    normalize(entry.title).includes(query));
}
export function entriesForWeek(data,date,options={}){
  const dates=weekDates(date);
  return filterPlanEntries(data,{...options,start:dates[0],end:dates[6]});
}
/* Verificación conservadora: únicamente el consumidor del catálogo puede acreditar vigencia.
   No convierte títulos o rutas almacenados en URLs. */
export function recipeReferenceStatus(entry,catalogRecord){
  const item=validatePlanEntry(entry);
  if(item.source.type==="free_text")return "not_applicable";
  if(!catalogRecord)return "unavailable";
  if(catalogRecord.id!==item.source.recipe_id||
     catalogRecord.source_commit!==item.source.source_commit||
     catalogRecord.source_path!==item.source.source_path)return "changed";
  return "verified";
}
