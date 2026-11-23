import {addEntry,editEntry,removeEntry,filterEntries,selectedMentions,dateRelation} from "./culinary-pantry-model.3ef4cae485d21026eed8.mjs";
import {createPantryPersistence,MAX_JSON_LENGTH} from "./culinary-pantry-persistence.3ef4cae485d21026eed8.mjs";

import {putMentions} from "./culinary-pantry-transfer.3ef4cae485d21026eed8.mjs";

const $=id=>document.getElementById(id);
const store=createPantryPersistence(()=>window.localStorage);
const locations={pantry:"Despensa",fridge:"Frigorífico",freezer:"Congelador",other:"Otra"};
const dateTypes={expiry:"Caducidad",best_before:"Consumo preferente"};
const relations={past:"Anterior a hoy",today:"Hoy",future:"Posterior a hoy"};
let data=null,ready=false,editing=null,preview=null,importGeneration=0;
const selected=new Set();
function el(tag,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;}
function button(text,action){const n=el("button",text,"secondary");n.type="button";n.disabled=!ready;n.addEventListener("click",action);return n;}
function announce(text){$("status").textContent=text;}
function today(){const d=new Date();return [String(d.getFullYear()).padStart(4,"0"),String(d.getMonth()+1).padStart(2,"0"),String(d.getDate()).padStart(2,"0")].join("-");}
function clearImport(){importGeneration++;preview=null;$("import-file").value="";$("import-preview").textContent="";syncControls();}
function syncControls(){
  $("entry-controls").disabled=!ready;$("filter-controls").disabled=!data;
  $("import-file").disabled=!ready;$("import-confirm").disabled=!ready||!preview;
  $("import-cancel").disabled=!preview;$("export").disabled=store.snapshot()===null;
}
function resetEditor(){
  editing=null;$("entry-form").reset();$("entry-heading").textContent="Añadir alimento";
  $("save-entry").textContent="Añadir alimento";$("cancel-edit").hidden=true;
}
function handleError(error){
  if(["conflict","blocked","read","not_ready"].includes(error?.code)){ready=false;clearImport();render();}
  announce(error instanceof Error?error.message:"No se pudo completar la operación.");
  syncControls();
}
function load(){
  ready=false;clearImport();resetEditor();selected.clear();
  try{const result=store.load();data=result.data;ready=true;announce(result.status==="absent"?"Todavía no hay alimentos guardados.":"Inventario recuperado.");}
  catch(error){data=store.snapshot();announce(error.message+" No se ha sustituido el inventario. "+(data?"Se muestra la última copia válida disponible.":""));}
  render();syncControls();
}
function save(next,message){
  try{data=store.save(next);announce(message);return true;}
  catch(error){handleError(error);return false;}
}
function newId(){
  if(globalThis.crypto?.randomUUID)return crypto.randomUUID();
  throw Error("No se puede generar un ID seguro. Abre la página mediante HTTPS o localhost.");
}
const optional=id=>$(id).value.trim()||null;
function readEntry(){
  return {id:editing??newId(),name:$("name").value.trim(),quantity:optional("quantity")?.replace(",",".")??null,
    unit:optional("unit"),category:optional("category"),location:$("location").value,
    date_type:optional("date-type"),date:optional("date"),notes:optional("notes")};
}
function startEdit(entry){
  if(!ready)return;
  editing=entry.id;
  for(const key of ["name","quantity","unit","category","location","date","notes"])$(key).value=entry[key]??"";
  $("date-type").value=entry.date_type??"";
  $("entry-heading").textContent="Editar alimento";$("save-entry").textContent="Guardar cambios";
  $("cancel-edit").hidden=false;$("name").focus();
}
function drop(entry){
  if(!ready||!confirm("¿Eliminar esta entrada de "+entry.name+"?"))return;
  try{if(save(removeEntry(data,entry.id),"Entrada eliminada.")){
    selected.delete(entry.id);if(editing===entry.id)resetEditor();render();
  }}catch(error){handleError(error);}
}
function renderSelection(){
  const list=$("selection");list.replaceChildren();
  const available=new Set(data?.entries.map(e=>e.id)??[]);
  for(const id of selected)if(!available.has(id))selected.delete(id);
  let names=[];
  if(selected.size){
    try{names=selectedMentions(data,[...selected]);}
    catch(error){list.append(el("li",error.message));}
  }
  for(const name of names)list.append(el("li",name));
  $("selection-count").textContent=selected.size+" entradas seleccionadas · "+names.length+" menciones";
  $("clear-selection").disabled=!selected.size;
  $("search-recipes").disabled=!ready||!names.length;
}
function card(entry){
  const article=el("article",undefined,"inventory-entry");article.append(el("h3",entry.name));
  article.append(el("p",entry.quantity===null?"Cantidad no declarada":entry.quantity+" "+entry.unit));
  article.append(el("p",locations[entry.location]+(entry.category?" · "+entry.category:""),"meta"));
  if(entry.date!==null){
    const relation=dateRelation(entry.date,today());
    article.append(el("p",dateTypes[entry.date_type]+": "+entry.date+" · "+relations[relation],relation==="past"?"date-past":""));
  }else article.append(el("p","Sin fecha declarada","meta"));
  if(entry.notes)article.append(el("p",entry.notes,"entry-notes"));
  const label=el("label",undefined,"select-entry"),check=el("input");check.type="checkbox";check.checked=selected.has(entry.id);
  check.disabled=!ready;check.addEventListener("change",()=>{if(check.checked)selected.add(entry.id);else selected.delete(entry.id);renderSelection();});
  label.append(check,el("span","Seleccionar "+entry.name));article.append(label);
  const actions=el("div",undefined,"actions");actions.append(button("Editar",()=>startEdit(entry)),button("Eliminar",()=>drop(entry)));
  article.append(actions);return article;
}
function render(){
  const list=$("inventory"),categories=$("categories"),filter=$("filter-category");
  const previous=filter.value;
  categories.replaceChildren();filter.replaceChildren(new Option("Todas",""));
  if(!data){list.replaceChildren();$("inventory-count").textContent="Inventario no disponible.";renderSelection();syncControls();return;}
  for(const value of [...new Set(data.entries.map(e=>e.category).filter(Boolean))].sort((a,b)=>a.localeCompare(b,"es"))){
    const option=el("option");option.value=value;categories.append(option);filter.add(new Option(value,value));
  }
  if([...filter.options].some(o=>o.value===previous))filter.value=previous;
  const rows=filterEntries(data,{name:$("filter-name").value,category:optional("filter-category"),location:optional("filter-location"),relation:optional("filter-date"),today:today()});
  list.replaceChildren(...rows.map(card));
  $("inventory-count").textContent=!data.entries.length?"Inventario vacío.":!rows.length?"Ninguna entrada coincide con los filtros.":rows.length+" de "+data.entries.length+" entradas";
  renderSelection();syncControls();
}
$("entry-form").addEventListener("submit",event=>{
  event.preventDefault();if(!ready)return;
  try{
    const entry=readEntry(),next=editing?editEntry(data,editing,entry):addEntry(data,entry);
    if(save(next,editing?"Cambios guardados.":"Alimento guardado.")){resetEditor();render();$("name").focus();}
  }catch(error){handleError(error);}
});
$("cancel-edit").addEventListener("click",()=>{resetEditor();$("name").focus();});
$("filters").addEventListener("input",render);
$("filters").addEventListener("submit",e=>e.preventDefault());
$("filters").addEventListener("reset",()=>setTimeout(render,0));
$("clear-selection").addEventListener("click",()=>{selected.clear();render();});
$("search-recipes").addEventListener("click",()=>{
  if(!ready)return;
  try{putMentions(()=>window.sessionStorage,selectedMentions(data,[...selected]));window.location.assign("culinary-explorer.html");}
  catch(error){announce(error.message);}
});
$("reload").addEventListener("click",()=>{if(editing!==null&&!confirm("¿Descartar la edición y recargar?"))return;load();});
$("export").addEventListener("click",()=>{
  try{
    const url=URL.createObjectURL(new Blob([store.exportLastValid()],{type:"application/json"}));
    const a=el("a");a.href=url;a.download="novacoquinaria-despensa-"+today()+".json";document.body.append(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);announce("Copia JSON preparada para descargar.");
  }catch(error){handleError(error);}
});
$("import-file").addEventListener("change",async()=>{
  const file=$("import-file").files[0];preview=null;const generation=++importGeneration;syncControls();
  $("import-preview").textContent="";
  if(!ready||!file)return;
  try{
    if(file.size>MAX_JSON_LENGTH*4)throw Error("Archivo demasiado grande.");
    const raw=await file.text();if(generation!==importGeneration||!ready)return;
    preview=store.previewImport(raw);
    $("import-preview").textContent="La copia contiene "+preview.count+" entradas. Sustituirá todo el inventario actual.";
    syncControls();
  }catch(error){if(generation===importGeneration){$("import-preview").textContent=error.message;syncControls();}}
});
$("import-cancel").addEventListener("click",()=>{clearImport();announce("Importación cancelada.");});
$("import-confirm").addEventListener("click",()=>{
  if(!ready||!preview||!confirm("¿Sustituir todo el inventario por "+preview.count+" entradas?"))return;
  try{data=store.confirmImport(preview,true).data;clearImport();resetEditor();selected.clear();render();announce("Inventario importado.");}
  catch(error){handleError(error);}
});
window.addEventListener("storage",event=>{
  if(store.observeStorageEvent(event)){ready=false;clearImport();render();announce("El inventario cambió en otra pestaña. Recarga antes de guardar.");}
});
load();
