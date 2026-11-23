/* Transporte efímero de intención explícita, no constituye una receta validada. */
export const SELECTION_KEY="novacoquinaria.planner.recipe-selection";
export function validateSelection(value){
  if(value===null||typeof value!=="object"||Array.isArray(value)||
    Object.keys(value).length!==1||!Object.hasOwn(value,"recipe_id")||
    typeof value.recipe_id!=="string"||!/^[A-Za-z0-9_-]{1,80}$/.test(value.recipe_id))
    throw Error("Selección de receta incompatible.");
  return {recipe_id:value.recipe_id};
}
export function storeSelection(getStorage,recipeId){
  const raw=JSON.stringify(validateSelection({recipe_id:recipeId}));
  try{getStorage().setItem(SELECTION_KEY,raw);}catch{throw Error("No se pudo guardar la selección temporal.");}
}
export function consumeSelection(getStorage){
  let raw;
  try{const storage=getStorage();raw=storage.getItem(SELECTION_KEY);if(raw!==null)storage.removeItem(SELECTION_KEY);}
  catch{throw Error("No se pudo leer la selección temporal.");}
  if(raw===null)return null;
  if(raw.length>1000)throw Error("Selección de receta demasiado grande.");
  try{return validateSelection(JSON.parse(raw));}catch{throw Error("Selección de receta inválida.");}
}
export function selectCatalogRecord(catalog,recipeId){
  if(catalog===null||typeof catalog!=="object"||!Array.isArray(catalog.recipes)||
     typeof catalog.source_commit!=="string"||!/^[a-f0-9]{40}$/.test(catalog.source_commit)||
     typeof recipeId!=="string")throw Error("Catálogo no disponible.");
  const rows=catalog.recipes.filter(r=>r.id===recipeId);
  if(rows.length!==1)throw Error("La receta seleccionada ya no está disponible en el catálogo.");
  const r=rows[0];
  const s=r.source_path;
  if(typeof r.title!=="string"||!r.title.trim()||r.title.length>160||
     typeof s!=="string"||s.length>500||!/^([0-9]{2}_[^/?#\\]+)\/([^/?#\\]+\.md)$/u.test(s)||
     s.split("/").some(v=>v==="."||v===".."||v.includes("%"))||
     typeof r.href!=="string"||r.href!==(s.slice(0,-3).split("/").map(encodeURIComponent).join("/")+".html").replace(/[!'()*]/g,c=>"%"+c.charCodeAt(0).toString(16).toUpperCase()))
    throw Error("La ficha de receta tiene un destino incoherente.");
  return {id:r.id,title:r.title,source_commit:catalog.source_commit,source_path:s,href:r.href};
}
