import {addList,renameList,removeList,addItem,editItem,removeItem,markPurchased,filterItems} from "./culinary-shopping-model.mjs";
import {createShoppingPersistence,MAX_JSON_LENGTH} from "./culinary-shopping-persistence.mjs";
const $=id=>document.getElementById(id);
const store=createShoppingPersistence(()=>window.localStorage);
let data=null,ready=false,active=null,editing=null,preview=null,generation=0;
const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
const announce=message=>{$("status").textContent=message;};
const list=()=>data?.lists.find(l=>l.id===active);
const optional=id=>$(id).value.trim()||null;
function newId(){if(globalThis.crypto?.randomUUID)return crypto.randomUUID();throw Error("Se requiere HTTPS o localhost para crear identificadores.");}
function controls(){
  $("list-controls").disabled=!ready;$("item-controls").disabled=!ready||!list();
  $("rename-controls").disabled=!ready||!list();$("import-file").disabled=!ready;
  $("import-confirm").disabled=!ready||!preview;$("import-cancel").disabled=!preview;
  $("export").disabled=store.snapshot()===null;
  $("delete-list").disabled=!ready||!list()||list().items.some(i=>i.transfer!==null);
}
function resetEditor(){editing=null;$("item-form").reset();$("item-heading").textContent="Añadir artículo";$("save-item").textContent="Añadir artículo";$("cancel-edit").hidden=true;}
function clearImport(){generation++;preview=null;$("import-file").value="";$("import-preview").textContent="";controls();}
function error(e){
  if(["conflict","blocked","read","not_ready"].includes(e?.code)){ready=false;clearImport();render();}
  announce(e instanceof Error?e.message:"No se pudo completar la operación.");controls();
}
function save(next,message){try{data=store.save(next);announce(message);return true;}catch(e){error(e);return false;}}
function load(){
  ready=false;clearImport();resetEditor();
  try{const result=store.load();data=result.data;ready=true;announce(result.status==="absent"?"Todavía no hay listas guardadas.":"Listas recuperadas.");}
  catch(e){data=store.snapshot();announce(e.message+" No se ha sustituido el documento."+(data?" Se muestra la última copia válida.":""));}
  render();
}
function selectList(id){
  if(active===id)return;
  if(editing!==null&&!confirm("¿Descartar la edición actual?"))return;
  active=id;resetEditor();$("filters").reset();render();$("active-title").focus();
}
function action(label,callback,disabled=false){const b=el("button",label,"secondary");b.type="button";b.disabled=disabled;b.addEventListener("click",callback);return b;}
function startEdit(item){
  if(!ready||item.transfer!==null)return;
  editing=item.id;
  for(const key of ["quantity","unit","category","notes"])$(key).value=item[key]??"";
  $("item-name").value=item.name;$("item-heading").textContent="Editar artículo";$("save-item").textContent="Guardar cambios";$("cancel-edit").hidden=false;$("item-name").focus();
}
function card(item){
  const locked=item.transfer!==null,article=el("article",undefined,"item-card"+(item.purchased?" purchased":""));
  article.append(el("h3",item.name),el("p",item.quantity===null?"Cantidad no declarada":item.quantity+" "+item.unit));
  if(item.category)article.append(el("p",item.category,"meta"));
  if(item.notes)article.append(el("p",item.notes,"notes"));
  if(item.provenance){const d=el("details");d.append(el("summary","Procedencia de receta"),el("p",item.provenance.recipe_id+" · líneas "+item.provenance.source_location.start_line+"–"+item.provenance.source_location.end_line),el("p",item.provenance.raw),el("p","Commit: "+item.provenance.source_commit,"meta"));article.append(d);}
  const label=el("label",undefined,"purchase-check"),check=el("input");check.type="checkbox";check.checked=item.purchased;check.disabled=!ready||locked;
  check.addEventListener("change",()=>{try{if(save(markPurchased(data,active,item.id,check.checked),check.checked?"Artículo marcado como comprado.":"Artículo pendiente de compra.")){if(editing===item.id)resetEditor();render();}else check.checked=item.purchased;}catch(e){check.checked=item.purchased;error(e);}});
  label.append(check,el("span","Comprado: "+item.name));article.append(label);
  if(locked)article.append(el("p",item.transfer.state==="pending"?"Transferencia pendiente de revisión. Registro protegido.":"Transferencia registrada. No acredita existencias actuales. Registro protegido.","help"));
  const actions=el("div",undefined,"actions");
  actions.append(action("Editar",()=>startEdit(item),!ready||locked),action("Eliminar",()=>{if(!ready||!confirm("¿Eliminar "+item.name+" de la lista?"))return;try{if(save(removeItem(data,active,item.id),"Artículo eliminado.")){if(editing===item.id)resetEditor();render();}}catch(e){error(e);}},!ready||locked));
  article.append(actions);return article;
}
function renderItems(){
  const current=list();if(!current)return;
  const category=$("filter-category"),previous=category.value;category.replaceChildren(new Option("Todas",""));$("categories").replaceChildren();
  for(const value of [...new Set(current.items.map(i=>i.category).filter(Boolean))].sort((a,b)=>a.localeCompare(b,"es"))){category.add(new Option(value,value));const option=el("option");option.value=value;$("categories").append(option);}
  if([...category.options].some(o=>o.value===previous))category.value=previous;
  const purchased=optional("filter-purchased");
  const rows=filterItems(data,active,{name:$("filter-name").value,category:optional("filter-category"),purchased:purchased===null?null:purchased==="true",transfer:optional("filter-transfer")});
  $("items").replaceChildren(...rows.map(card));
  $("items-count").textContent=!current.items.length?"Lista vacía.":!rows.length?"Ningún artículo coincide con los filtros.":rows.length+" de "+current.items.length+" artículos";
}
function render(){
  if(!list())active=data?.lists[0]?.id??null;
  $("lists").replaceChildren();
  for(const l of data?.lists??[]){const count=l.items.filter(i=>i.purchased).length;const b=action(l.name+" · "+count+"/"+l.items.length,()=>selectList(l.id));b.classList.add("list-choice");b.setAttribute("aria-pressed",String(active===l.id));$("lists").append(b);}
  $("lists-count").textContent=data?(data.lists.length?data.lists.length+" listas":"No hay listas. Crea una para comenzar."):"Listas no disponibles.";
  const current=list();$("active-section").hidden=!current;
  if(current){$("active-title").textContent=current.name;$("rename-name").value=current.name;
    const count=current.items.filter(i=>i.purchased).length;$("progress").textContent=count+" de "+current.items.length+" artículos comprados";$("progress-bar").max=Math.max(1,current.items.length);$("progress-bar").value=count;
    $("list-lock").textContent=current.items.some(i=>i.transfer!==null)?"Esta lista conserva registros de transferencia y no puede eliminarse.":"";
    renderItems();}
  controls();
}
$("list-form").addEventListener("submit",e=>{e.preventDefault();if(!ready)return;if(editing!==null&&!confirm("¿Descartar la edición actual?"))return;try{const id=newId();if(save(addList(data,id,$("list-name").value.trim()),"Lista creada.")){active=id;resetEditor();$("list-form").reset();$("filters").reset();render();$("item-name").focus();}}catch(e){error(e);}});
$("rename-form").addEventListener("submit",e=>{e.preventDefault();if(!ready||!list())return;try{if(save(renameList(data,active,$("rename-name").value.trim()),"Lista renombrada."))render();}catch(e){error(e);}});
$("delete-list").addEventListener("click",()=>{if(!ready||!list()||!confirm("¿Eliminar la lista y todos sus artículos?"))return;try{if(save(removeList(data,active),"Lista eliminada.")){active=null;resetEditor();$("filters").reset();render();}}catch(e){error(e);}});
$("item-form").addEventListener("submit",e=>{
  e.preventDefault();if(!ready||!list())return;
  try{const previous=editing===null?null:list().items.find(i=>i.id===editing);
    if(editing!==null&&!previous)throw Error("Artículo desconocido.");
    const item={id:previous?.id??newId(),name:$("item-name").value.trim(),quantity:optional("quantity")?.replace(",",".")??null,unit:optional("unit"),category:optional("category"),notes:optional("notes"),purchased:previous?.purchased??false,provenance:previous?.provenance??null,transfer:null};
    if(save(previous?editItem(data,active,editing,item):addItem(data,active,item),previous?"Cambios guardados.":"Artículo añadido.")){resetEditor();render();$("item-name").focus();}
  }catch(e){error(e);}
});
$("cancel-edit").addEventListener("click",()=>{resetEditor();$("item-name").focus();});
$("filters").addEventListener("input",renderItems);$("filters").addEventListener("submit",e=>e.preventDefault());$("filters").addEventListener("reset",()=>setTimeout(renderItems,0));
$("reload").addEventListener("click",()=>{if(editing!==null&&!confirm("¿Descartar la edición y recargar?"))return;load();});
$("export").addEventListener("click",()=>{try{const url=URL.createObjectURL(new Blob([store.exportLastValid()],{type:"application/json"})),a=el("a");a.href=url;a.download="novacoquinaria-compras.json";document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);announce("Copia JSON preparada para descargar.");}catch(e){error(e);}});
$("import-file").addEventListener("change",async()=>{const file=$("import-file").files[0],token=++generation;preview=null;controls();$("import-preview").textContent="";if(!file||!ready)return;
  try{if(file.size>MAX_JSON_LENGTH*4)throw Error("Archivo demasiado grande.");const raw=await file.text();if(token!==generation||!ready)return;preview=store.previewImport(raw);$("import-preview").textContent="La copia contiene "+preview.listCount+" listas y "+preview.itemCount+" artículos. Sustituirá las listas actuales.";controls();}
  catch(e){if(token===generation){$("import-preview").textContent=e.message;controls();}}
});
$("import-cancel").addEventListener("click",()=>{clearImport();announce("Importación cancelada.");});
$("import-confirm").addEventListener("click",()=>{if(!ready||!preview||!confirm("¿Sustituir todas las listas por la copia seleccionada?"))return;try{data=store.confirmImport(preview,true).data;clearImport();active=null;resetEditor();$("filters").reset();render();announce("Listas importadas.");}catch(e){error(e);}});
window.addEventListener("storage",event=>{if(store.observeStorageEvent(event)){ready=false;clearImport();render();announce("Las listas cambiaron en otra pestaña. Recarga antes de guardar.");}});
load();
