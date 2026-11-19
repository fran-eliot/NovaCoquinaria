/* Selección de ocurrencias procedentes de una receta cargada; sin inferir cantidades. */
import {validateItem} from "./culinary-shopping-model.mjs";
export const RECIPE_TRANSFER_KEY="novacoquinaria.shopping.recipe-selection";
function validate(payload){
  if(!payload||payload.version!=="0.1.0"||typeof payload.title!=="string"||!payload.title.trim()||payload.title.length>500||
     !Array.isArray(payload.items)||!payload.items.length||payload.items.length>2000)throw Error("Selección de receta inválida.");
  const seen=new Set();let identity=null;
  const items=payload.items.map((x,i)=>{
    const item=validateItem({id:"review-"+i,name:x.name,quantity:null,unit:null,category:null,notes:null,purchased:false,provenance:x.provenance,transfer:null});
    const p=item.provenance;
    if(!p||seen.has(p.position)||identity!==null&&identity!==p.recipe_id+":"+p.source_commit)throw Error("Procedencia de selección incoherente.");
    identity=p.recipe_id+":"+p.source_commit;seen.add(p.position);
    return {name:item.name,provenance:p};
  });
  return {version:"0.1.0",title:payload.title,items};
}
export function createRecipeSelection(recipe,positions){
  if(!Array.isArray(positions)||!positions.length||new Set(positions).size!==positions.length)throw Error("Selecciona ingredientes concretos.");
  const items=positions.map(pos=>{
    const e=recipe.ingredients[pos];
    if(!Number.isInteger(pos)||pos<0||!e||e.position!==pos)throw Error("Ocurrencia desconocida.");
    return {name:(e.name||e.raw).trim().slice(0,160),provenance:{recipe_id:recipe.id,position:pos,
      source_location:{start_line:e.source_location.start_line,end_line:e.source_location.end_line},raw:e.raw,source_commit:recipe.source_commit}};
  });
  return validate({version:"0.1.0",title:recipe.title,items});
}
export function putRecipeSelection(getStorage,payload){
  const raw=JSON.stringify(validate(payload));
  if(raw.length>12000000)throw Error("Selección demasiado grande.");
  try{getStorage().setItem(RECIPE_TRANSFER_KEY,raw);}catch{throw Error("No se pudo guardar la selección temporal.");}
}
export function takeRecipeSelection(getStorage){
  const storage=getStorage(),raw=storage.getItem(RECIPE_TRANSFER_KEY);
  if(raw===null)return null;
  storage.removeItem(RECIPE_TRANSFER_KEY);
  if(typeof raw!=="string"||raw.length>12000000)throw Error("Selección inválida.");
  return validate(JSON.parse(raw));
}
