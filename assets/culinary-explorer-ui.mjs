import {createSearch} from "./culinary-explorer-search.mjs";

const $ = id => document.getElementById(id);
const modules = {"01_Arroces":"Arroces","02_Pastas":"Pastas","03_Legumbres":"Legumbres",
  "04_Verduras":"Verduras","05_Carnes":"Carnes","06_Pescados_y_Mariscos":"Pescados y mariscos",
  "07_Cocina_Asiatica":"Cocina asiática","08_Postres":"Postres","09_Bebidas":"Bebidas","10_Horno":"Horno"};
const evidence = {prepared:"Elaboración registrada",pending:"Pendiente de prueba",unknown:"Evidencia desconocida"};
const optionality = {required:"Requerido",optional:"Opcional",unknown:"Opcionalidad desconocida"};
const pageSize = 24;
let engine, catalog, rows = [], page = 0;

function element(tag, content, className) {
  const node = document.createElement(tag);
  if (content !== undefined) node.textContent = content;
  if (className) node.className = className;
  return node;
}

export function recipeHref(recipe) {
  const path = recipe.source_path;
  if (typeof path !== "string" || !Object.hasOwn(modules, recipe.physical_module) ||
      !path.startsWith(recipe.physical_module + "/") || !path.endsWith(".md") ||
      /[\\:#?\u0000-\u001f\u007f]/u.test(path) ||
      path.split("/").some(p => !p || p === "." || p === "..") ||
      path.split("/").at(-1) === "README.md") throw new Error("Ruta inválida");
  const expected = path.slice(0,-3).split("/").map(encodeURIComponent).join("/") + ".html";
  // Python quote codifica también estos caracteres admitidos por encodeURIComponent.
  const href = expected.replace(/[!'()*]/g, c => "%" + c.charCodeAt(0).toString(16).toUpperCase());
  if (recipe.href !== href) throw new Error("Destino incoherente");
  return href;
}

function validateCatalog(data) {
  if (!data || !Array.isArray(data.recipes) ||
      !/^[a-f0-9]{40}$/.test(data.source_commit) || !/^[a-f0-9]{64}$/.test(data.index_sha256))
    throw new Error("Procedencia inválida");
  const strings = value => Array.isArray(value) && value.every(v => typeof v === "string");
  const ids = new Set(), paths = new Set();
  for (const recipe of data.recipes) {
    if (typeof recipe.id !== "string" || !recipe.id || ids.has(recipe.id) ||
        paths.has(recipe.source_path) || typeof recipe.title !== "string" || !recipe.title ||
        typeof recipe.title_key !== "string" || !strings(recipe.title_tokens) ||
        !Object.hasOwn(evidence, recipe.evidence?.status) || !Array.isArray(recipe.ingredients))
      throw new Error("Registro inválido");
    recipeHref(recipe);
    recipe.ingredients.forEach((entry, i) => {
      if (entry.position !== i || !strings(entry.tokens) ||
          !(entry.name === null || typeof entry.name === "string") ||
          typeof entry.raw !== "string" || !Object.hasOwn(optionality, entry.optionality) ||
          !Number.isInteger(entry.source_location?.start_line) ||
          !Number.isInteger(entry.source_location?.end_line) ||
          entry.source_location.start_line < 1 ||
          entry.source_location.end_line < entry.source_location.start_line)
        throw new Error("Ocurrencia inválida");
    });
    ids.add(recipe.id); paths.add(recipe.source_path);
  }
  return createSearch(data);
}

function card({recipe,matches}) {
  const article = element("article");
  const title = element("h3");
  const link = element("a", recipe.title);
  link.setAttribute("href", recipeHref(recipe));
  title.append(link); article.append(title);
  article.append(element("p", modules[recipe.physical_module] + " · " + evidence[recipe.evidence.status], "meta"));
  const params = new URLSearchParams({id:recipe.id});
  const cook = element("a","Preparar receta","prepare-link");
  // Un enlace corto debe abrir la aplicación actual y no una página antigua en caché.
  cook.href = "recipe-assistant.html?" + params.toString();
  article.append(cook);
  if (matches.length) {
    const details = element("details");
    details.append(element("summary","Ver menciones coincidentes"));
    for (const match of matches) {
      details.append(element("p", "Consulta: " + match.value));
      const ul = element("ul");
      for (const entry of match.occurrences) {
        ul.append(element("li", entry.raw + " · " + optionality[entry.optionality] +
          " · línea de origen " + entry.source_location.start_line));
      }
      details.append(ul);
    }
    article.append(details);
  }
  return article;
}

function render() {
  const total = rows.length;
  const count = Math.ceil(total / pageSize);
  $("results-section").hidden = total === 0;
  $("results").replaceChildren(...rows.slice(page*pageSize,(page+1)*pageSize).map(card));
  $("pagination").hidden = count <= 1;
  $("page").textContent = "Página " + (page+1) + " de " + count;
  $("prev").disabled = page === 0;
  $("next").disabled = page+1 >= count;
  $("status").textContent = total ? total + " recetas de " + catalog.recipe_count +
    " · mostrando " + (page*pageSize+1) + "–" + Math.min(total,(page+1)*pageSize) :
    catalog.recipe_count === 0 ? "El catálogo está vacío." : "No hay recetas que coincidan con los filtros.";
}

function run() {
  try {
    rows = engine.search({title: $("title").value.trim() || null,
      titleMode: $("title-mode").value,
      ingredients: $("ingredients").value.split(/\r?\n/).map(s=>s.trim()).filter(Boolean),
      module: $("module").value || null, evidence: $("evidence").value || null});
    page = 0;
    render();
  } catch (error) {
    rows = []; page = 0;
    $("results").replaceChildren();
    $("results-section").hidden = true;
    $("status").textContent = "Consulta inválida. Revisa los términos e inténtalo de nuevo.";
  }
}

async function init() {
  try {
    const response = await fetch(new URL("../culinary_explorer.json", import.meta.url), {cache:"no-cache"});
    if (!response.ok) throw new Error("Catálogo no disponible");
    catalog = await response.json();
    engine = validateCatalog(catalog);
    for (const [value,label] of Object.entries(modules)) {
      if (!engine.modules.includes(value)) continue;
      const option = element("option",label);
      option.value = value;
      $("module").append(option);
    }
    $("provenance").textContent = "Fuente: catálogo del commit " + catalog.source_commit +
      " · esquema " + catalog.schema_version;
    $("controls").disabled = false;
    run();
  } catch (error) {
    $("status").textContent = "No se pudo cargar el catálogo completo. Recarga la página o vuelve al portal.";
  }
}

$("filters").addEventListener("submit", event => {event.preventDefault(); run();});
$("filters").addEventListener("reset", () => setTimeout(run,0));
$("prev").addEventListener("click", () => {if(page>0){page--;render();$("results-heading").focus();}});
$("next").addEventListener("click", () => {if((page+1)*pageSize<rows.length){page++;render();$("results-heading").focus();}});
init();
