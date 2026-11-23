/* Nota de preparación local y exportable; no modifica la ficha ni conserva datos. */
const trim = value => typeof value === "string" ? value.trim() : "";
const quoted = value => (trim(value) || "No documentado").split(/\r?\n/).map(line => "> " + line.replace(/\r/g, "")).join("\n");

export function feedbackMarkdown(recipe, values) {
  if (!recipe || !/^REC-\d+$/.test(recipe.id) || !trim(recipe.title) ||
      !trim(recipe.source_path) || !/^[a-f0-9]{40}$/.test(recipe.source_commit))
    throw new Error("Referencia de receta inválida");
  if (!values || !["confirmada", "no_confirmada"].includes(values.status))
    throw new Error("Estado de preparación inválido");
  for (const key of ["result", "differences", "proposal", "preference"])
    if (typeof values[key] !== "string" || values[key].length > 5000)
      throw new Error("Nota inválida o demasiado extensa");
  if (!["result", "differences", "proposal", "preference"].some(key => trim(values[key])))
    throw new Error("Escribe alguna observación antes de exportar");
  return [
    "# Observación de preparación — " + recipe.title,
    "",
    "- Receta: " + recipe.id,
    "- Fuente canónica: " + recipe.source_path,
    "- Commit de referencia: " + recipe.source_commit,
    "- Estado declarado: " + (values.status === "confirmada" ?
      "Preparación confirmada por quien redacta esta nota" :
      "Preparación no confirmada; anotaciones y propuestas sin prueba acreditada"),
    "- Fecha efectiva de preparación: no documentada",
    "- Procedencia: declaración del usuario de esta exportación, pendiente de revisión editorial",
    "",
    "## Resultado observado o comentario",
    quoted(values.result), "",
    "## Diferencias realmente realizadas o recordadas",
    quoted(values.differences), "",
    "## Mejor versión y variantes",
    quoted(values.preference), "",
    "## Propuesta pendiente de probar",
    quoted(values.proposal), "",
    "Esta nota no modifica la receta ni confirma automáticamente una elaboración, una valoración o la seguridad alimentaria.",
    "Revisar la procedencia y comparar variantes antes de incorporarla al Markdown canónico.",
    ""
  ].join("\n");
}

export function mountPreparationFeedback(recipe, host = document.getElementById("assistant")) {
  if (!host) throw new Error("Contenedor del asistente no disponible");
  const panel = document.createElement("section");
  panel.className = "panel";
  panel.id = "preparation-feedback";
  panel.setAttribute("aria-labelledby", "preparation-feedback-heading");
  const heading = document.createElement("h2");
  heading.id = "preparation-feedback-heading";
  heading.textContent = "Notas tras la preparación";
  const intro = document.createElement("p");
  intro.textContent = "Exporta una nota para revisar después. No se guarda ni se envía; una propuesta no equivale a una prueba realizada.";
  panel.append(heading, intro);
  const fields = {};
  function field(id, labelText, multiline = true) {
    const wrapper = document.createElement("div");
    wrapper.className = "feedback-field";
    const label = document.createElement("label");
    label.htmlFor = "feedback-" + id;
    label.textContent = labelText;
    const control = document.createElement(multiline ? "textarea" : "select");
    control.id = label.htmlFor;
    if (multiline) {
      control.rows = 3;
      control.maxLength = 5000;
    } else {
      for (const [value, text] of [
        ["no_confirmada", "Sin elaboración confirmada"],
        ["confirmada", "La he preparado realmente"]
      ]) {
        const option = document.createElement("option");
        option.value = value; option.textContent = text; control.append(option);
      }
    }
    wrapper.append(label, control);
    panel.append(wrapper);
    fields[id] = control;
  }
  field("status", "¿Has preparado esta receta?", false);
  field("result", "Resultado y valoración (solo si constan)");
  field("differences", "Cambios que realmente realizaste o recuerdas");
  field("preference", "Mejor versión conocida y variantes");
  field("proposal", "Ajustes propuestos pendientes de probar");
  const download = document.createElement("button");
  download.type = "button";
  download.id = "feedback-export";
  download.textContent = "Exportar nota Markdown";
  const message = document.createElement("p");
  message.id = "feedback-message";
  message.setAttribute("role", "status");
  download.addEventListener("click", () => {
    try {
      const values = Object.fromEntries(Object.entries(fields).map(([key, control]) => [key, control.value]));
      const markdown = feedbackMarkdown(recipe, values);
      const url = URL.createObjectURL(new Blob([markdown], {type: "text/markdown;charset=utf-8"}));
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = "observacion-" + recipe.id + ".md";
      panel.append(anchor);
      anchor.click();
      anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      message.textContent = "Nota exportada. Revísala antes de proponer cambios en el repositorio.";
    } catch (error) {
      message.textContent = error instanceof Error ? error.message : "No se pudo exportar la nota";
    }
  });
  panel.append(download, message);
  host.append(panel);
  return panel;
}
