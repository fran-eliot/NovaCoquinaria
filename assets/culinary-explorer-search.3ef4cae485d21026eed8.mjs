/* Adaptador puro de consultas de Culinary Explorer. Sin DOM ni red. */
export function createSearch(catalog) {
  if (catalog.schema_version !== "0.1.1" ||
      catalog.index_version !== "0.2.0" ||
      !Array.isArray(catalog.recipes) || catalog.recipe_count !== catalog.recipes.length) {
    throw new Error("Catálogo incompatible");
  }
  const profile = catalog.unicode_profile;
  if (!profile || !profile.casefold || !Array.isArray(profile.spaces) ||
      !Array.isArray(profile.alnum_ranges)) throw new Error("Perfil Unicode incompatible");
  const spaces = new Set(profile.spaces);
  const ranges = profile.alnum_ranges;
  function alnum(cp) {
    let lo = 0, hi = ranges.length - 1;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      const [a, b] = ranges[mid];
      if (cp < a) hi = mid - 1;
      else if (cp > b) lo = mid + 1;
      else return true;
    }
    return false;
  }
  function key(value) {
    if (typeof value !== "string") throw new Error("Consulta no textual");
    let out = "", pending = false;
    for (const c of value) {
      for (const ch of profile.casefold[c.codePointAt(0)] ?? c) {
        if (spaces.has(ch.codePointAt(0))) {
          pending = out.length > 0;
        } else {
          if (pending) out += " ";
          out += ch;
          pending = false;
        }
      }
    }
    return out.normalize("NFC");
  }
  function tokens(value) {
    const result = [];
    let term = "";
    for (const c of key(value)) {
      if (alnum(c.codePointAt(0))) term += c;
      else if (term) { result.push(term); term = ""; }
    }
    if (term) result.push(term);
    return result;
  }
  function contains(hay, needle) {
    return needle.length > 0 && hay.some((_, i) =>
      i + needle.length <= hay.length && needle.every((word, j) => word === hay[i+j]));
  }
  const statuses = new Set(["prepared", "pending", "unknown"]);
  const modules = new Set(catalog.recipes.map(r => r.physical_module));
  function search({title = null, titleMode = "terms", ingredients = [],
                   module = null, evidence = null} = {}) {
    if (!["exact", "terms"].includes(titleMode) || !Array.isArray(ingredients) ||
        (module !== null && typeof module !== "string") ||
        (evidence !== null && !statuses.has(evidence))) throw new Error("Filtros inválidos");
    const titleQuery = title === null ? null : titleMode === "exact" ? key(title) : tokens(title);
    if (titleQuery !== null && !titleQuery.length) throw new Error("Título vacío");
    const clauses = ingredients.map(value => {
      const needle = tokens(value);
      if (!needle.length) throw new Error("Ingrediente sin términos");
      return needle;
    });
    const result = [];
    for (const recipe of catalog.recipes) {
      if (module !== null && recipe.physical_module !== module) continue;
      if (evidence !== null && recipe.evidence.status !== evidence) continue;
      if (titleQuery !== null && !(titleMode === "exact" ?
          recipe.title_key === titleQuery : contains(recipe.title_tokens, titleQuery))) continue;
      const matches = clauses.map((needle, i) => ({
        value: ingredients[i], match_scope: "textual_mention",
        occurrences: recipe.ingredients.filter(entry => contains(entry.tokens, needle))
      }));
      if (matches.every(match => match.occurrences.length)) result.push({recipe, matches});
    }
    return result;
  }
  return {search, key, tokens, modules: [...modules], evidence: [...statuses]};
}
