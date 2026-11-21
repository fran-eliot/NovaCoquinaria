import {addPlanEntry,editPlanEntry,removePlanEntry,filterPlanEntries,
  weekDates,weekStart,shiftCivilDate,validCivilDate} from "./culinary-planner-model.mjs";
import {createPlannerPersistence,MAX_JSON_LENGTH} from "./culinary-planner-persistence.mjs";

const $=id=>document.getElementById(id);
const store=createPlannerPersistence(()=>window.localStorage);
const meals=[["breakfast","Desayuno"],["lunch","Comida"],["dinner","Cena"],["other","Otro"]];
const weekdays=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"];
const node=(tag,value,cls)=>{const element=document.createElement(tag);if(value!==undefined)element.textContent=value;if(cls)element.className=cls;return element;};
const message=text=>{$("status").textContent=text;};
const civilToday=()=>{
  const d=new Date();return String(d.getFullYear()).padStart(4,"0")+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");
};
let data=null,ready=false,chosen=civilToday(),editing=null,preview=null,request=0;
function weekFor(date){return weekDates(date);}
function button(text,callback,disabled=false){
  const b=node("button",text,"secondary");b.type="button";b.disabled=disabled;b.addEventListener("click",callback);return b;
}
function controls(){
  $("entry-controls").disabled=!ready;$("import-file").disabled=!ready;
  $("import-confirm").disabled=!ready||preview===null;
  $("import-cancel").disabled=preview===null;
  $("export").disabled=store.snapshot()===null;
  $("week-previous").disabled=!canShift(chosen,-7);
  $("week-next").disabled=!canShift(chosen,7);
  $("day-previous").disabled=!canShift(chosen,-1);
  $("day-next").disabled=!canShift(chosen,1);
}
function canShift(date,delta){
  try{weekFor(shiftCivilDate(date,delta));return true;}catch{return false;}
}
function cancelPreview(){
  ++request;preview=null;$("import-file").value="";$("import-preview").textContent="";controls();
}
function resetEditor(){
  editing=null;$("entry-form").reset();$("editor-heading").textContent="Añadir un plato libre";
  $("entry-save").textContent="Añadir al plan";$("entry-cancel").hidden=true;
  $("entry-date").value=chosen;
}
function freeze(error){
  ready=false;cancelPreview();render();
  message(error instanceof Error?error.message:"No se pudo guardar. Recarga los datos para continuar.");
}
function save(next,description){
  try{data=store.save(next);message(description);return true;}
  catch(error){if(["conflict","read","blocked","not_ready"].includes(error?.code))freeze(error);
    else message(error instanceof Error?error.message:"Error de almacenamiento.");
    return false;}
}
function load(){
  ready=false;cancelPreview();resetEditor();
  try{const result=store.load();data=result.data;ready=true;message(result.status==="absent"?"Aún no hay comidas guardadas.":"Plan cargado.");}
  catch(error){data=store.snapshot();message(error.message+" No se han reemplazado los datos."+(data?" Se muestra la última copia válida.":""));}
  render();
}
function selectDay(date){
  if(editing!==null&&!confirm("¿Descartar los cambios de la edición actual?"))return;
  chosen=date;resetEditor();render();$("day-heading").focus();
}
function changeDay(delta){
  try{const date=shiftCivilDate(chosen,delta);weekFor(date);selectDay(date);}
  catch{message("La fecha solicitada está fuera del calendario disponible.");}
}
function renderWeek(){
  let dates;
  try{dates=weekFor(chosen);}
  catch{chosen=civilToday();dates=weekFor(chosen);}
  $("week-range").textContent=dates[0]+" — "+dates[6];
  const grid=$("week-grid");
  grid.replaceChildren();
  for(let i=0;i<dates.length;i++){
    const date=dates[i],count=(data?.entries??[]).filter(e=>e.date===date).length;
    const b=button(weekdays[i]+" "+date.slice(8)+" · "+count,()=>selectDay(date));
    b.replaceChildren(node("span",weekdays[i].slice(0,3),"week-day"),node("span",date.slice(8),"week-date"),
      node("span",count+" comidas","week-count"));
    b.setAttribute("aria-label",weekdays[i]+" "+date+": "+count+" entradas");
    b.setAttribute("aria-pressed",String(chosen===date));
    grid.append(b);
  }
}
function startEdit(entry){
  if(!ready)return;
  if(editing!==null&&editing!==entry.id&&!confirm("¿Descartar la edición actual?"))return;
  editing=entry.id;
  $("editor-heading").textContent="Editar entrada del plan";
  $("entry-save").textContent="Guardar cambios";$("entry-cancel").hidden=false;
  $("entry-date").value=entry.date;$("entry-meal").value=entry.meal;
  $("entry-title").value=entry.title;$("entry-notes").value=entry.notes??"";
  $("entry-title").focus();
}
function drawEntry(entry){
  const article=node("article",undefined,"plan-entry");
  article.append(node("h4",entry.title),node("p",entry.source.type==="recipe"?"Receta documentada (referencia pendiente de verificar)":"Plato libre","meta"));
  if(entry.notes!==null)article.append(node("p",entry.notes,"plan-notes"));
  const actions=node("div",undefined,"actions");
  actions.append(button("Editar",()=>startEdit(entry),!ready));
  actions.append(button("Eliminar",()=>{
    if(!ready||!confirm("¿Eliminar "+entry.title+" del plan del "+entry.date+"?"))return;
    try{if(save(removePlanEntry(data,entry.id),"Comida eliminada.")){if(editing===entry.id)resetEditor();render();}}
    catch(e){message(e.message);}
  },!ready));
  article.append(actions);
  return article;
}
function renderDay(){
  $("day-heading").textContent="Comidas del "+chosen;
  $("day-entries").replaceChildren();
  if(data===null){$("day-count").textContent="Plan no disponible.";return;}
  const entries=filterPlanEntries(data,{start:chosen,end:chosen,
    meal:$("filter-meal").value||null,title:$("filter-title").value});
  const total=data.entries.filter(e=>e.date===chosen).length;
  $("day-count").textContent=total===0?"No hay comidas planificadas para este día.":entries.length+" de "+total+" entradas visibles.";
  if(!entries.length){$("day-entries").append(node("p",total?"Ninguna comida coincide con los filtros.":"Añade una comida para comenzar.","help"));return;}
  for(const [meal,label] of meals){
    const list=entries.filter(entry=>entry.meal===meal);if(!list.length)continue;
    const section=node("section",undefined,"meal-group"),container=node("div",undefined,"meal-entries");
    section.append(node("h3",label));container.append(...list.map(drawEntry));section.append(container);
    $("day-entries").append(section);
  }
}
function render(){renderWeek();renderDay();controls();}
$("entry-form").addEventListener("submit",event=>{
  event.preventDefault();if(!ready)return;
  try{
    const original=editing===null?null:data.entries.find(e=>e.id===editing);
    if(editing!==null&&!original)throw Error("La entrada editada ya no existe.");
    const date=$("entry-date").value;
    if(!validCivilDate(date))throw Error("Introduce una fecha civil válida.");
    weekFor(date);
    const entry={id:original?.id??crypto.randomUUID(),date,meal:$("entry-meal").value,title:$("entry-title").value.trim(),
      notes:$("entry-notes").value.trim()||null,source:original?.source??{type:"free_text"}};
    const next=original?editPlanEntry(data,original.id,entry):addPlanEntry(data,entry);
    if(save(next,original?"Comida actualizada.":"Comida añadida.")){chosen=date;resetEditor();render();$("entry-title").focus();}
  }catch(error){message(error.message);}
});
$("entry-cancel").addEventListener("click",()=>{resetEditor();$("entry-title").focus();});
$("filter-form").addEventListener("input",renderDay);
$("filter-form").addEventListener("submit",e=>e.preventDefault());
$("filter-form").addEventListener("reset",()=>{queueMicrotask(renderDay);});
$("week-previous").addEventListener("click",()=>changeDay(-7));
$("week-next").addEventListener("click",()=>changeDay(7));
$("day-previous").addEventListener("click",()=>changeDay(-1));
$("day-next").addEventListener("click",()=>changeDay(1));
$("week-today").addEventListener("click",()=>{try{selectDay(civilToday());}catch(e){message(e.message);}});
$("reload").addEventListener("click",()=>{
  if(editing!==null&&!confirm("¿Descartar la edición actual y recargar?"))return;load();
});
$("export").addEventListener("click",()=>{
  try{
    const url=URL.createObjectURL(new Blob([store.exportLastValid()],{type:"application/json"}));
    const a=node("a");a.href=url;a.download="novacoquinaria-planificador.json";document.body.append(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);
    message("Copia JSON preparada para descargar.");
  }catch(error){message(error.message);}
});
$("import-file").addEventListener("change",async()=>{
  const file=$("import-file").files[0],token=++request;preview=null;controls();
  $("import-preview").textContent="";
  if(!file||!ready)return;
  try{
    if(file.size>MAX_JSON_LENGTH*4)throw Error("El archivo es demasiado grande.");
    const raw=await file.text();
    if(token!==request||!ready)return;
    preview=store.previewImport(raw);
    $("import-preview").textContent="Copia válida: "+preview.count+" entradas. Sustituirá el plan actual si confirmas.";
    controls();
  }catch(error){if(token===request){$("import-preview").textContent=error.message;controls();}}
});
$("import-cancel").addEventListener("click",()=>{
  try{store.confirmImport(preview,false);}catch{}cancelPreview();message("Importación cancelada.");
});
$("import-confirm").addEventListener("click",()=>{
  if(!ready||preview===null||!confirm("¿Sustituir el plan completo por la copia revisada?"))return;
  try{
    data=store.confirmImport(preview,true).data;cancelPreview();resetEditor();render();message("Plan importado.");
  }catch(error){if(["conflict","blocked","read","not_ready"].includes(error?.code))freeze(error);else message(error.message);}
});
window.addEventListener("storage",event=>{
  if(store.observeStorageEvent(event)){
    ready=false;cancelPreview();render();message("El plan cambió en otra pestaña. Recarga para continuar.");
  }
});
load();
