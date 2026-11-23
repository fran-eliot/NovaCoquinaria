/* Nota de preparación local y exportable; no modifica la ficha ni conserva datos. */
const trim = value => typeof value === "string" ? value.trim() : "";
const quoted = value => (trim(value) || "No documentado").split(/\r?\n/).map(line => "> " + line.replace(/\r/g, "")).join("\n");

export function feedbackMarkdown(recipe, values) {
  if (!recipe || !/^REC-\d+$/.test(recipe.id) || !trim(recipe.title) ||
      !trim(recipe.source_path) || !/^[a-f0-9]{40}$/.test(recipe.source_commit))
    throw new Error("Referencia de receta inválida");
  if (!values || !["confirmada", "no_confirmada"].includes(values.status))
    throw new Error("Estado de preparación inválido");
  const date = trim(values.date);
  if (date) {
    if (values.status !== "confirmada" || !/^\d{4}-\d{2}-\d{2}$/.test(date))
      throw new Error("Indica una fecha válida de una preparación confirmada");
    const parsed = new Date(date + "T00:00:00Z");
    if (!Number.isFinite(parsed.getTime()) || parsed.toISOString().slice(0, 10) !== date)
      throw new Error("Fecha de elaboración inválida");
  }
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
    "- Fecha efectiva de preparación: " + (date || "no documentada"),
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
    return wrapper;
  }
  field("status", "¿Has preparado esta receta?", false);
  const dateWrapper = document.createElement("div");
  dateWrapper.className = "feedback-field";
  const dateLabel = document.createElement("label");
  dateLabel.htmlFor = "feedback-date";
  dateLabel.textContent = "Fecha real de elaboración (opcional, solo si se conoce)";
  const dateInput = document.createElement("input");
  dateInput.id = dateLabel.htmlFor;
  dateInput.type = "date";
  dateInput.disabled = true;
  fields.status.addEventListener("change", () => {
    dateInput.disabled = fields.status.value !== "confirmada";
    if (dateInput.disabled) dateInput.value = "";
  });
  dateWrapper.append(dateLabel, dateInput);
  panel.append(dateWrapper);
  fields.date = dateInput;
  field("result", "Resultado y valoración (solo si constan)");
  field("differences", "Cambios que realmente realizaste o recuerdas");
  const optional = document.createElement("details");
  optional.id = "feedback-optional";
  optional.className = "feedback-optional";
  const optionalSummary = document.createElement("summary");
  optionalSummary.textContent = "Variantes y propuestas (opcional)";
  optional.append(optionalSummary);
  optional.append(
    field("preference", "Mejor versión conocida y variantes"),
    field("proposal", "Ajustes propuestos pendientes de probar")
  );
  panel.append(optional);
  const download = document.createElement("button");
  download.type = "button";
  download.id = "feedback-export";
  download.textContent = "Exportar nota Markdown";
  const message = document.createElement("p");
  message.id = "feedback-message";
  message.setAttribute("role", "status");
  const note = () => feedbackMarkdown(recipe,
    Object.fromEntries(Object.entries(fields).map(([key, control]) => [key, control.value])));
  download.addEventListener("click", () => {
    try {
      const markdown = note();
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
  const copy = document.createElement("button");
  copy.type = "button";
  copy.id = "feedback-copy";
  copy.textContent = "Copiar nota Markdown";
  copy.addEventListener("click", async () => {
    try {
      const markdown = note();
      if (!navigator.clipboard?.writeText) throw new Error("Portapapeles no disponible");
      await navigator.clipboard.writeText(markdown);
      message.textContent = "Nota copiada. Revísala antes de incorporarla al recetario.";
    } catch (error) {
      message.textContent = error instanceof Error ? error.message : "No se pudo copiar la nota";
    }
  });
  const previewButton = document.createElement("button");
  previewButton.type = "button";
  previewButton.id = "feedback-preview-button";
  previewButton.textContent = "Revisar nota Markdown";
  const preview = document.createElement("pre");
  preview.id = "feedback-preview";
  preview.hidden = true;
  preview.setAttribute("aria-label", "Vista previa de la nota Markdown");
  const invalidate = () => {
    preview.hidden = true;
    preview.textContent = "";
  };
  for (const control of Object.values(fields)) {
    control.addEventListener("input", invalidate);
    control.addEventListener("change", invalidate);
  }
  previewButton.addEventListener("click", () => {
    try {
      preview.textContent = note();
      preview.hidden = false;
      message.textContent = "Vista previa actualizada.";
    } catch (error) {
      invalidate();
      message.textContent = error instanceof Error ? error.message : "No se pudo generar la vista previa";
    }
  });
  panel.append(previewButton, download, copy, message, preview);
  host.append(panel);
  return panel;
}
