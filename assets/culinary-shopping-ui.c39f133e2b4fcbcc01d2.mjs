import {addList,renameList,removeList,addItem,editItem,removeItem,markPurchased,filterItems} from "./culinary-shopping-model.c39f133e2b4fcbcc01d2.mjs";
import {createShoppingPersistence,MAX_JSON_LENGTH} from "./culinary-shopping-persistence.c39f133e2b4fcbcc01d2.mjs";
import {takeRecipeSelection} from "./culinary-shopping-recipe-transfer.c39f133e2b4fcbcc01d2.mjs";
import {createPantryPersistence} from "./culinary-pantry-persistence.c39f133e2b4fcbcc01d2.mjs";
import {transferPurchased,recoverTransfer} from "./culinary-shopping-pantry-coordinator.c39f133e2b4fcbcc01d2.mjs";
import {validateEntry} from "./culinary-pantry-model.c39f133e2b4fcbcc01d2.mjs";
const $=id=>document.getElementById(id);
const store=createShoppingPersistence(()=>window.localStorage);
const pantry=createPantryPersistence(()=>window.localStorage);
let transferReview=null,transferBusy=false;
let recipeReview=null,reviewRows=[];
let data=null,ready=false,active=null,editing=null,preview=null,generation=0;
const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
const announce=message=>{$("status").textContent=message;};
const list=()=>data?.lists.find(l=>l.id===active);
const optional=id=>$(id).value.trim()||null;
function newId(){if(globalThis.crypto?.randomUUID)return crypto.randomUUID();throw Error("Se requiere HTTPS o localhost para crear identificadores.");}
function controls(){
  $("reload").disabled=transferBusy;
  $("list-controls").disabled=!ready;$("item-controls").disabled=!ready||!list();
  $("rename-controls").disabled=!ready||!list();$("import-file").disabled=!ready;
  $("import-confirm").disabled=!ready||!preview;$("import-cancel").disabled=!preview;
  $("export").disabled=store.snapshot()===null;
  $("review-confirm").disabled=!ready||!recipeReview||!data?.lists.length;
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
  if(item.purchased&&!locked)actions.append(action("Incorporar a despensa",()=>openTransfer(item),!ready||!navigator.locks));
  if(item.transfer?.state==="pending"){
    const t=item.transfer.entry,d=el("details");d.append(el("summary","Destino revisado"),el("p",t.name+" · "+(t.quantity===null?"Cantidad no declarada":t.quantity+" "+t.unit)),el("p","Ubicación: "+t.location+" · "+(t.date??"Sin fecha")),el("p","ID: "+t.id,"meta"));
    if(t.category)d.append(el("p","Categoría: "+t.category));
    if(t.notes)d.append(el("p",t.notes,"notes"));
    if(t.date_type)d.append(el("p","Tipo de fecha: "+t.date_type));
    article.append(d);
    actions.append(action("Verificar transferencia pendiente",()=>recover(item),!ready||!navigator.locks));
  }
  actions.append(action("Editar",()=>startEdit(item),!ready||locked),action("Eliminar",()=>{if(!ready||!confirm("¿Eliminar "+item.name+" de la lista?"))return;try{if(save(removeItem(data,active,item.id),"Artículo eliminado.")){if(editing===item.id)resetEditor();render();}}catch(e){error(e);}},!ready||locked));
  article.append(actions);return article;
}
function openTransfer(item){
  if(!ready||transferBusy||!navigator.locks)return;
  transferReview={listId:active,itemId:item.id,expected:data};
  $("transfer-form").reset();
  for(const k of ["name","quantity","unit","category","notes"])$("transfer-"+k).value=item[k]??"";
  $("transfer-feedback").textContent="";
  $("transfer-dialog").showModal();
  $("transfer-location").focus();
}
function readTransfer(){
  return validateEntry({id:"shopping-"+transferReview.itemId,name:$("transfer-name").value.trim(),
    quantity:optional("transfer-quantity")?.replace(",",".")??null,unit:optional("transfer-unit"),
    category:optional("transfer-category"),notes:optional("transfer-notes"),location:$("transfer-location").value,
    date_type:optional("transfer-date-type"),date:optional("transfer-date")});
}
async function executeTransfer(operation,args){
  if(!ready||transferBusy)return;
  if(!navigator.locks){announce("Este navegador no permite coordinar transferencias entre pestañas.");return;}
  transferBusy=true;ready=false;render();
  try{
    const result=await navigator.locks.request("novacoquinaria.shopping-pantry-transfer",{ifAvailable:true},lock=>{
      if(!lock)throw Error("Hay otra transferencia en curso. Revisa el estado antes de continuar.");
      return operation({shopping:store,pantry,...args,confirmed:true});
    });
    data=result.data;ready=true;announce("Transferencia registrada en la despensa.");
  }catch(e){
    // Releer el estado persistido, incluso cuando el segundo guardado falló.
    try{data=store.load().data;ready=true;}
    catch{data=store.snapshot();ready=false;}
    announce("No se completó la transferencia: "+(e instanceof Error?e.message:"Error desconocido.")+" Revisa el estado; no se ha repetido ninguna escritura.");
  }finally{transferBusy=false;render();}
}
function recover(item){
  if(!ready||transferBusy)return;
  if(!confirm("¿Verificar el lote registrado? No se creará ningún alimento nuevo."))return;
  void executeTransfer(recoverTransfer,{expected:data,listId:active,itemId:item.id});
}
$("transfer-form").addEventListener("submit",event=>{
  event.preventDefault();
  if(!transferReview||!ready||transferBusy)return;
  try{
    const entry=readTransfer(),review=transferReview;
    if(!confirm("¿Crear este lote en la despensa y proteger el registro de compra?"))return;
    $("transfer-dialog").close();transferReview=null;
    void executeTransfer(transferPurchased,{...review,entry});
  }catch(e){$("transfer-feedback").textContent=e.message;}
});
$("transfer-cancel").addEventListener("click",()=>{$("transfer-dialog").close();});
$("transfer-dialog").addEventListener("close",()=>{transferReview=null;});
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
  updateReviewLists();controls();
}
function updateReviewLists(){
  const select=$("review-list"),previous=select.value;
  select.replaceChildren(...(data?.lists??[]).map(l=>new Option(l.name,l.id)));
  if([...select.options].some(o=>o.value===previous))select.value=previous;
}
function renderRecipeReview(){
  $("recipe-review").hidden=!recipeReview;
  if(!recipeReview)return;
  $("review-source").textContent=recipeReview.title+" · "+recipeReview.items[0].provenance.recipe_id;
  $("review-items").replaceChildren();reviewRows=[];
  for(const x of recipeReview.items){
    const field=el("fieldset"),legend=el("legend",x.provenance.raw),label=el("label",undefined,"purchase-check"),check=el("input");
    check.type="checkbox";check.checked=true;label.append(check,el("span","Incluir artículo"));field.append(legend,label);
    const fields={};
    for(const [key,title,max,value] of [["name","Nombre",160,x.name],["quantity","Cantidad",16,""],["unit","Unidad",40,""]]){
      const l=el("label",title),input=el("input");input.maxLength=max;input.value=value;if(key==="quantity")input.inputMode="decimal";l.append(input);field.append(l);fields[key]=input;
    }
    $("review-items").append(field);reviewRows.push({check,fields,provenance:x.provenance});
  }
  updateReviewLists();controls();
}
$("review-cancel").addEventListener("click",()=>{recipeReview=null;reviewRows=[];$("recipe-review").hidden=true;controls();});
$("review-form").addEventListener("submit",e=>{
  e.preventDefault();if(!ready||!recipeReview)return;
  try{
    const chosen=reviewRows.filter(x=>x.check.checked),destination=$("review-list").value;
    if(!chosen.length)throw Error("Selecciona al menos un artículo.");
    if(!confirm("¿Añadir "+chosen.length+" artículos revisados a la lista?"))return;
    let next=data;
    for(const x of chosen)next=addItem(next,destination,{id:newId(),name:x.fields.name.value.trim(),quantity:x.fields.quantity.value.trim().replace(",",".")||null,unit:x.fields.unit.value.trim()||null,category:null,notes:null,purchased:false,provenance:x.provenance,transfer:null});
    if(save(next,"Ingredientes añadidos a la lista.")){recipeReview=null;reviewRows=[];$("recipe-review").hidden=true;active=destination;resetEditor();$("filters").reset();render();}
  }catch(e){$("review-status").textContent=e.message;}
});
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
window.addEventListener("storage",event=>{if(store.observeStorageEvent(event)){ready=false;if($("transfer-dialog").open)$("transfer-dialog").close();clearImport();render();announce("Las listas cambiaron en otra pestaña. Recarga antes de guardar.");}});
load();
try{recipeReview=takeRecipeSelection(()=>window.sessionStorage);renderRecipeReview();}catch(e){announce("No se pudo recuperar la selección de receta.");}
