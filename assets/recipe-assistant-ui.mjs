import {storeSelection} from "./culinary-planner-recipe-transfer.mjs";
import {createCookingSession, createManualTimer} from "./recipe-assistant-session.mjs";
import {mountPreparationFeedback} from "./recipe-assistant-feedback.mjs";
import {scalingBasis, scaleIngredient, formatScaledList} from "./recipe-assistant-scaling.mjs";

import {createRecipeSelection,putRecipeSelection} from "./culinary-shopping-recipe-transfer.mjs";
import {inline, renderMarkdown} from "./recipe-assistant-markdown.mjs";

const $ = id => document.getElementById(id);
const evidenceLabels = {prepared:"Elaboración registrada",pending:"Pendiente de prueba",unknown:"Evidencia desconocida"};
const optionality = {required:"Requerido",optional:"Opcional",unknown:"Opcionalidad desconocida"};
const phases = {preparation:"Preparación",cooking:"Cocinado",baking:"Horneado",rest:"Reposo",chilling:"Refrigeración",declared_total:"Tiempo declarado",marinating:"Marinado"};
const modules = new Set(["01_Arroces","02_Pastas","03_Legumbres","04_Verduras","05_Carnes","06_Pescados_y_Mariscos","07_Cocina_Asiatica","08_Postres","09_Bebidas","10_Horno"]);
const hash = (s,n) => typeof s==="string" && s.length===n && /^[a-f0-9]+$/.test(s);
const nonempty = s => typeof s==="string" && s.trim().length>0;
const obj = o => o!==null && typeof o==="object" && !Array.isArray(o);
const check = (condition,message="Datos incompatibles") => {if(!condition) throw new Error(message);};

function node(tag,text,cls) {
  const el=document.createElement(tag);
  if(text!==undefined) el.textContent=text;
  if(cls) el.className=cls;
  return el;
}
function link(label,href) {const a=node("a",label);a.setAttribute("href",href);return a;}
function safeHref(path,technique=false) {
  check(nonempty(path) && path.endsWith(".md") && !/[\\:#?\u0000-\u001f\u007f]/u.test(path) &&
    path.split("/").every(v=>v && v!=="." && v!=="..") &&
    (technique?path.startsWith("00_Bases/03_Tecnicas/"):modules.has(path.split("/")[0])),"Ruta inválida");
  return (path.slice(0,-3).split("/").map(encodeURIComponent).join("/")+".html")
    .replace(/[!'()*]/g,c=>"%"+c.charCodeAt(0).toString(16).toUpperCase());
}
const base=new URL("../",import.meta.url);
async function bytes(url) {
  const response=await fetch(url,{cache:"no-cache"});
  check(response.ok,"Recurso no disponible");
  return await response.arrayBuffer();
}
const parse = buffer => JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(buffer));
async function sha256(buffer) {
  check(globalThis.crypto?.subtle,"Se requiere un contexto seguro");
  return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",buffer)),v=>v.toString(16).padStart(2,"0")).join("");
}

export async function loadRecipe(params) {
  const id=params.get("id"), legacyCommit=params.get("commit"), legacyIndex=params.get("index");
  const legacy=params.has("commit")||params.has("index");
  check(params.getAll("id").length===1 && nonempty(id) && (!legacy || (params.getAll("commit").length===1 &&
    params.getAll("index").length===1 && hash(legacyCommit,40) && hash(legacyIndex,64))),
    "Selecciona una receta desde el explorador");
  const manifest=parse(await bytes(new URL("recipe_assistant/manifest.json",base)));
  check(obj(manifest) && manifest.schema_version==="0.1.0" && manifest.index_version==="0.2.0" &&
    hash(manifest.source_commit,40) && hash(manifest.index_sha256,64) &&
    (!legacy || (manifest.source_commit===legacyCommit && manifest.index_sha256===legacyIndex)) && obj(manifest.recipes) &&
    manifest.recipe_count===Object.keys(manifest.recipes).length,"Catálogo desactualizado; vuelve al explorador");
  const commit=manifest.source_commit, index=manifest.index_sha256;
  check(Object.hasOwn(manifest.recipes,id),"Receta desconocida");
  const entry=manifest.recipes[id];
  const filename=await sha256(new TextEncoder().encode(id))+".json";
  check(obj(entry) && entry.file===filename && hash(entry.sha256,64) && hash(entry.source_sha256,64));
  const raw=await bytes(new URL("recipe_assistant/"+filename,base));
  check(await sha256(raw)===entry.sha256,"Huella de receta incorrecta");
  const recipe=parse(raw);
  check(obj(recipe) && recipe.schema_version==="0.1.0" && recipe.index_version===manifest.index_version &&
    recipe.id===id && recipe.source_commit===commit && recipe.index_sha256===index &&
    recipe.source_sha256===entry.source_sha256 && nonempty(recipe.title) &&
    recipe.href===entry.href && recipe.href===safeHref(recipe.source_path));
  check(obj(recipe.context) && recipe.context.mode==="full_source" && nonempty(recipe.context.text));
  const last=recipe.context.source_location?.end_line;
  const loc=l=>obj(l) && Number.isInteger(l.start_line) && Number.isInteger(l.end_line) &&
    l.start_line>=1 && l.end_line>=l.start_line && l.end_line<=last;
  check(Number.isInteger(last) && loc(recipe.context.source_location));
  const nullableText=v=>v===null || typeof v==="string";
  for(const key of ["ingredients","steps","durations","mise_en_place","techniques","diagnostics"])
    check(Array.isArray(recipe[key]));
  for(const e of recipe.ingredients) check(obj(e) && nonempty(e.raw) && nullableText(e.name) &&
    nullableText(e.group) && obj(e.quantity) && Object.hasOwn(optionality,e.optionality) && loc(e.source_location));
  for(const s of recipe.steps) check(obj(s) && nonempty(s.text) && loc(s.source_location));
  for(const d of [...recipe.durations,...(recipe.yield===null?[]:[recipe.yield])])
    check(obj(d) && nonempty(d.raw) && loc(d.source_location));
  for(const s of recipe.mise_en_place) check(obj(s) && nullableText(s.heading) &&
    typeof s.content==="string" && loc(s.source_location));
  for(const t of recipe.techniques) check(obj(t) && nonempty(t.label) && loc(t.source_location) &&
    t.href===safeHref(t.source_path,true));
  check(obj(recipe.evidence) && Object.hasOwn(evidenceLabels,recipe.evidence.status) &&
    Array.isArray(recipe.evidence.claims) && recipe.evidence.claims.every(c=>obj(c)&&nonempty(c.text)&&loc(c.source_location)));
  return recipe;
}
function line(l){return "Fuente: líneas "+l.start_line+"–"+l.end_line;}
function renderRecipe(r) {
  const session=createCookingSession(r), timer=createManualTimer();
  $("recipe-title").textContent=r.title;
  $("plan-recipe").addEventListener("click",()=>{
    if(!confirm("¿Abrir el planificador? Se perderá el progreso de preparación de esta página."))return;
    try{storeSelection(()=>window.sessionStorage,r.id);location.assign("culinary-planner.html");}
    catch(error){$("load-status").textContent=error.message;}
  });
  document.title=r.title+" | NovaCoquinaria";
  $("source-link").href=r.href;
  $("evidence").textContent=evidenceLabels[r.evidence.status]+" · No equivale a validación de la fórmula actual.";
  for(const c of r.evidence.claims) $("claims").append(inline(node("p",undefined,"source-text meta"),c.text+" · "+line(c.source_location)));
  $("yield").textContent="Rendimiento: "+(r.yield?r.yield.raw:
    r.diagnostics.some(d=>d.code==="YIELD_AMBIGUOUS")?"Declaraciones ambiguas; consultar contexto.":"No declarado o no reconocido.");
  const originalServings=scalingBasis(r);
  function refreshShoppingScalingNote(){
    const desired=originalServings===null?null:$("scaling-target").valueAsNumber;
    const note=$("shopping-scaling-note");
    if(originalServings===null)note.textContent="Sin rendimiento escalable: Shopping recibirá los ingredientes originales, sin cantidades propuestas.";
    else if(!Number.isInteger(desired)||desired<1||desired>24)
      note.textContent="Raciones no válidas. Corrige el valor antes de enviar ingredientes a Shopping.";
    else if(desired===originalServings)
      note.textContent="Raciones originales ("+originalServings+"): Shopping recibirá los ingredientes originales, sin cantidades propuestas.";
    else note.textContent="Adaptación de "+originalServings+" a "+desired+" raciones: Shopping propondrá únicamente las cantidades escalables para revisarlas antes de guardarlas.";
  }
  refreshShoppingScalingNote();
  const inlineScaled=new Map();
  let refreshScaling=()=>{};
  if(originalServings!==null){
    $("scaling-panel").hidden=false;
    $("scaling-original").textContent=String(originalServings);
    const target=$("scaling-target"),preview=$("scaling-preview"),status=$("scaling-status"),copy=$("copy-scaling"),reset=$("scaling-reset");
    target.value=String(originalServings);
    function updateScaling(){
      preview.replaceChildren();
      const desired=target.valueAsNumber;
      refreshShoppingScalingNote();
      reset.disabled=target.value===String(originalServings);
      $("copy-scaling-status").textContent="";
      copy.disabled=true;
      if(!Number.isInteger(desired)||desired<1||desired>24){
        for(const hint of inlineScaled.values()){hint.hidden=true;hint.textContent="";}
        status.textContent="Indica entre 1 y 24 raciones.";return;
      }
      copy.disabled=false;
      const unchanged=desired===originalServings;
      let count=0;
      for(const entry of r.ingredients){
        const scaled=unchanged?null:scaleIngredient(entry,originalServings,desired);
        const li=node("li");
        if(unchanged)li.textContent=entry.raw;
        else if(scaled){li.textContent=entry.raw+" → "+scaled.quantity+" "+scaled.unit;count++;}
        else li.textContent=entry.raw+" — sin ajuste automático";
        const hint=inlineScaled.get(entry.position);
        if(hint){
          hint.hidden=!scaled || desired===originalServings;
          hint.textContent=scaled && desired!==originalServings?"Adaptado: "+scaled.quantity+" "+scaled.unit:"";
        }
        preview.append(li);
      }
      status.textContent=unchanged?"Raciones originales. Se muestran las cantidades declaradas sin ajustes.":
        count+" de "+r.ingredients.length+" cantidades ajustadas. Verifica ingredientes, proporciones y tiempos en la ficha original.";
    }
    refreshScaling=updateScaling;
    target.addEventListener("input",()=>{updateScaling();refreshShoppingSelection();});
    reset.addEventListener("click",()=>{
      target.value=String(originalServings);
      updateScaling();
      refreshShoppingSelection();
      target.focus();
    });
    copy.addEventListener("click",async()=>{
      copy.disabled=true;
      try{
        if(!navigator.clipboard?.writeText) throw new Error("Portapapeles no disponible");
        await navigator.clipboard.writeText(formatScaledList(r,target.valueAsNumber));
        $("copy-scaling-status").textContent="Lista copiada. Revisa las cantidades no ajustadas.";
      }catch{
        $("copy-scaling-status").textContent="No se pudo copiar. Comprueba los permisos del navegador.";
      }finally{
        const desired=target.valueAsNumber;
        copy.disabled=!(Number.isInteger(desired)&&desired>=1&&desired<=24);
      }
    });
    updateScaling();
  }
  for(const d of r.durations) $("durations").append(node("li",(Object.hasOwn(phases,d.phase)?phases[d.phase]:d.phase)+": "+d.raw));
  if(!r.durations.length) $("durations").append(node("li","Tiempos no declarados o no reconocidos."));
  const shoppingChecks=[];
  function refreshShoppingSelection(){
    const count=shoppingChecks.filter(x=>x.check.checked).length;
    $("shopping-count").textContent=count+" de "+shoppingChecks.length+" ingredientes seleccionados";
    const desired=originalServings===null?null:$("scaling-target").valueAsNumber;
    const validServings=desired===null || (Number.isInteger(desired)&&desired>=1&&desired<=24);
    const proposalStatus=$("shopping-proposals");
    if(count===0)proposalStatus.textContent="Selecciona ingredientes para consultar el alcance de la adaptación.";
    else if(!validServings)proposalStatus.textContent="Corrige las raciones antes de calcular las cantidades propuestas.";
    else if(originalServings===null || desired===originalServings)
      proposalStatus.textContent=count+" ingredientes con cantidades originales; no se propondrán ajustes automáticos.";
    else{
      const selected=shoppingChecks.filter(x=>x.check.checked);
      const proposals=selected.filter(x=>scaleIngredient(r.ingredients[x.position],originalServings,desired)!==null).length;
      proposalStatus.textContent=proposals+" de "+count+" ingredientes con cantidad propuesta; "+
        (count-proposals)+" requieren revisión manual en Shopping.";
    }
    $("send-shopping").disabled=count===0 || !validServings;
    $("shopping-select-all").disabled=shoppingChecks.length===0;
    $("shopping-select-required").disabled=!shoppingChecks.some(x=>x.optionality==="required");
    $("shopping-clear").disabled=count===0;
  }
  for(const e of r.ingredients){
    const label=node("label",undefined,"check-row"),check=node("input");
    check.type="checkbox";
    check.addEventListener("change",refreshShoppingSelection);
    label.append(check,node("span",e.raw));
    $("shopping-selection").append(label);
    shoppingChecks.push({check,position:e.position,optionality:e.optionality});
  }
  for(const [id,eligible] of [
    ["shopping-select-all",()=>true],
    ["shopping-select-required",x=>x.optionality==="required"],
    ["shopping-clear",()=>false]
  ]) $(id).addEventListener("click",()=>{
    for(const entry of shoppingChecks)entry.check.checked=eligible(entry);
    refreshShoppingSelection();
  });
  refreshShoppingSelection();
  $("send-shopping").addEventListener("click",()=>{
    try{
      const desired=originalServings===null?null:$("scaling-target").valueAsNumber;
      const selection=createRecipeSelection(r,shoppingChecks.filter(x=>x.check.checked).map(x=>x.position),
        {targetServings:desired});
      if(!confirm("¿Abrir compras? Se perderá el progreso de preparación de esta página."))return;
      putRecipeSelection(()=>window.sessionStorage,selection);location.assign("culinary-shopping.html");
    }catch(e){$("shopping-status").textContent=e.message;}
  });
  let group=null;
  const inputs=[];
  for(const e of r.ingredients) {
    if(e.group!==group){group=e.group;$("ingredients").append(node("h3",group??"Sin grupo"));}
    const label=node("label",undefined,"check-row"),input=node("input");
    input.type="checkbox";input.addEventListener("change",()=>{session.markIngredient(e.position,input.checked);progress();});
    const ingredientText=inline(node("span",undefined,"ingredient-text"),e.raw+" · "+optionality[e.optionality]);
    const hint=node("small",undefined,"scaled-ingredient-hint");
    hint.hidden=true;
    label.append(input,ingredientText,hint);
    $("ingredients").append(label);inputs.push(input);inlineScaled.set(e.position,hint);
  }
  if(!inputs.length) $("ingredients").append(node("p","No se reconocieron ingredientes; consulta la ficha."));
  refreshScaling();
  for(const s of r.mise_en_place) {
    if(s.heading) $("mise").append(node("h4",s.heading));
    const body=node("div");renderMarkdown(body,s.content);$("mise").append(body);
  }
  if(!r.mise_en_place.length) $("mise").append(node("p","No se reconoció una sección explícita."));
  for(const t of r.techniques){const li=node("li");li.append(link(t.label,t.href));$("techniques").append(li);}
  if(!r.techniques.length) $("techniques").append(node("li","Sin referencias a técnicas disponibles en esta vista."));
  renderMarkdown($("context-text"),r.context.text);
  mountPreparationFeedback(r);
  $("provenance").textContent=r.id+" · commit "+r.source_commit+" · esquema "+r.schema_version;
  for (const step of r.steps) {
    const option=node("option","Paso "+step.order);
    option.value=String(step.order);
    $("step-picker").append(option);
  }
  $("step-picker").addEventListener("change",()=>{
    const order=Number($("step-picker").value);
    session.goToStep(order);
    progress();$("step-title").focus();
  });
  function progress(){
    const s=session.snapshot();
    $("ingredient-progress").textContent=s.prepared.length+" de "+s.ingredientCount+" ingredientes marcados";
    $("step-progress").textContent=s.stepCount?s.completed.length+" de "+s.stepCount+" pasos marcados":"No se reconocieron pasos; consulta el contexto completo.";
    $("step-controls").hidden=s.current===null;
    if(s.current===null)return;
    const step=r.steps[s.current-1];
    for (const option of $("step-picker").options) {
      const order=Number(option.value);
      option.textContent="Paso "+order+" — "+(s.completed.includes(order)?"completado":"pendiente");
    }
    $("step-picker").value=String(s.current);
    $("step-title").textContent="Paso "+s.current+" de "+s.stepCount;
    renderMarkdown($("step-text"),step.text);
    $("step-location").textContent=line(step.source_location);
    $("step-done").checked=s.completed.includes(s.current);
    $("previous").disabled=s.current===1;$("next-step").disabled=s.current===s.stepCount;
    $("first-pending-step").disabled=session.firstPending()===null;
    $("complete-next-step").disabled=s.completed.includes(s.current);
  }
  $("step-done").addEventListener("change",()=>{session.markStep(session.snapshot().current,$("step-done").checked);progress();});
  for(const [id,delta] of [["previous",-1],["next-step",1]]) $(id).addEventListener("click",()=>{session.move(delta);progress();$("step-title").focus();});
  $("first-pending-step").addEventListener("click",()=>{session.jumpToFirstPending();progress();$("step-title").focus();});
  $("complete-next-step").addEventListener("click",()=>{
    const state=session.snapshot();
    if(state.current===null || state.completed.includes(state.current))return;
    session.markStep(state.current,true);
    if(state.current<state.stepCount)session.move(1);
    progress();$("step-title").focus();
  });
  let lastStatus=null;
  function refreshTimer(){
    const t=timer.snapshot(),active=t.status==="running"||t.status==="paused",sec=t.remainingSeconds;
    $("timer-display").textContent=[Math.floor(sec/3600),Math.floor(sec%3600/60),sec%60].map(n=>String(n).padStart(2,"0")).join(":");
    $("start-timer").disabled=active;$("minutes").disabled=active;$("seconds").disabled=active;
    $("pause-timer").disabled=t.status!=="running";$("resume-timer").disabled=t.status!=="paused";$("cancel-timer").disabled=t.status==="idle";
    if(lastStatus!==t.status){$("timer-status").textContent=({idle:"Inactivo",running:"En ejecución",paused:"Pausado",finished:"Tiempo finalizado. Comprueba el estado de la preparación."})[t.status];lastStatus=t.status;}
    $("timer-status").classList.toggle("timer-finished",t.status==="finished");
  }
  $("timer-form").addEventListener("submit",e=>{e.preventDefault();try{timer.start($("minutes").valueAsNumber,$("seconds").valueAsNumber);refreshTimer();}catch{ $("timer-status").textContent="Introduce una duración válida de al menos un segundo."; }});
  for(const [id,method] of [["pause-timer","pause"],["resume-timer","resume"],["cancel-timer","cancel"]])
    $(id).addEventListener("click",()=>{timer[method]();refreshTimer();});
  $("reset-session").addEventListener("click",()=>{
    if(!confirm("¿Reiniciar ingredientes, pasos y temporizador?"))return;
    session.reset();timer.cancel();inputs.forEach(i=>i.checked=false);progress();refreshTimer();
  });
  progress();refreshTimer();setInterval(refreshTimer,250);
  document.addEventListener("visibilitychange",refreshTimer);
}

async function init(){
  try{
    const recipe=await loadRecipe(new URLSearchParams(location.search));
    renderRecipe(recipe);
    const clean=new URL(location.href);clean.search=new URLSearchParams({id:recipe.id}).toString();
    history.replaceState(null,"",clean);
    $("assistant").hidden=false;$("load-status").textContent="Receta cargada.";
  }catch(error){
    $("assistant").hidden=true;
    $("load-status").textContent="No se pudo abrir la receta. Vuelve al explorador y selecciona de nuevo. "+(error instanceof Error?error.message:"");
  }
}
init();
