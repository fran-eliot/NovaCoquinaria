/* Vista de escalado conservadora: no altera fuente, estado ni compras. */
const UNITS = new Set(["g", "kg", "ml", "cl", "l"]);
const COUNT_UNITS = new Set(["unidad", "diente", "hoja", "rama"]);
const decimal = value => {
  if (typeof value !== "string") return null;
  // Las cantidades exactas del extractor pueden expresarse como fracciones.
  const fraction = /^(\d+)\/(\d+)$/.exec(value);
  if (fraction) {
    const numerator = Number(fraction[1]), denominator = Number(fraction[2]);
    if (!Number.isSafeInteger(numerator) || !Number.isSafeInteger(denominator) ||
        numerator <= 0 || denominator <= 0) return null;
    return numerator / denominator;
  }
  if (!/^(?:0|[1-9]\d*)(?:\.\d+)?$/.test(value)) return null;
  const n = Number(value);
  return Number.isFinite(n) && n > 0 ? n : null;
};
export function scalingBasis(recipe) {
  const y = recipe?.yield;
  if (!y || !["racion","porcion"].includes(y.unit) || y.min !== y.max) return null;
  const original = decimal(y.min);
  return original !== null && Number.isInteger(original) && original <= 24 ? original : null;
}
export function scaleIngredient(entry, originalServings, targetServings) {
  if (!Number.isInteger(originalServings) || originalServings < 1 || originalServings > 24 ||
      !Number.isInteger(targetServings) || targetServings < 1 || targetServings > 24) return null;
  const q = entry?.quantity;
  if (!q || q.status !== "exact" || q.approximate !== false || q.min !== q.max || !UNITS.has(q.unit) && !COUNT_UNITS.has(q.unit)) return null;
  const amount = decimal(q.min);
  if (amount === null) return null;
  const result = amount * targetServings / originalServings;
  if (!Number.isFinite(result) || result <= 0 || result > 1e7 ||
      (COUNT_UNITS.has(q.unit) && !Number.isSafeInteger(result))) return null;
  const rounded=Number(result.toFixed(3));
  if(!Number.isFinite(rounded) || rounded<=0) return null;
  return {quantity: rounded.toLocaleString("es-ES", {maximumFractionDigits:3}), unit:q.unit};
}

export function formatScaledList(recipe, targetServings) {
  const originalServings=scalingBasis(recipe);
  if(originalServings===null || !Number.isInteger(targetServings) ||
      targetServings<1 || targetServings>24 || !Array.isArray(recipe.ingredients))
    throw new Error("Raciones no válidas para exportar");
  const rows=[
    recipe.title+" — "+targetServings+" raciones (original: "+originalServings+")",
    "Cantidades orientativas. Revisar la ficha y los tiempos antes de cocinar.",
    ""
  ];
  for(const entry of recipe.ingredients){
    const scaled=scaleIngredient(entry,originalServings,targetServings);
    rows.push("- "+entry.raw+(targetServings===originalServings?"":scaled?
      " → "+scaled.quantity+" "+scaled.unit:" [revisar manualmente]"));
  }
  return rows.join("\n");
}
