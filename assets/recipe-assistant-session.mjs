/* Estado efímero de preparación. Independiente de DOM, almacenamiento y red. */
const MAX_SECONDS = 24 * 60 * 60 - 1;

function invariant(condition, message) {
  if (!condition) throw new Error(message);
}

export function createCookingSession(recipe) {
  invariant(recipe && typeof recipe.id === "string" && recipe.id.length &&
    Array.isArray(recipe.ingredients) && Array.isArray(recipe.steps), "Receta inválida");
  for (const [i, entry] of recipe.ingredients.entries())
    invariant(entry?.position === i, "Posición de ingrediente inválida");
  for (const [i, step] of recipe.steps.entries())
    invariant(step?.order === i + 1, "Orden de paso inválido");
  const ingredientCount = recipe.ingredients.length, stepCount = recipe.steps.length;
  const recipeId = recipe.id;
  const prepared = new Set(), completed = new Set();
  let current = stepCount ? 1 : null;
  const snapshot = () => ({
    recipeId, ingredientCount, stepCount, current,
    prepared: [...prepared].sort((a,b)=>a-b),
    completed: [...completed].sort((a,b)=>a-b)
  });
  function markIngredient(position, checked) {
    invariant(Number.isInteger(position) && position>=0 && position<ingredientCount &&
      typeof checked==="boolean", "Ingrediente inválido");
    if (checked) prepared.add(position); else prepared.delete(position);
    return snapshot();
  }
  function markStep(order, checked) {
    invariant(Number.isInteger(order) && order>=1 && order<=stepCount &&
      typeof checked==="boolean", "Paso inválido");
    if (checked) completed.add(order); else completed.delete(order);
    return snapshot();
  }
  function move(delta) {
    invariant(delta===1 || delta===-1, "Dirección inválida");
    if (current!==null) current=Math.max(1,Math.min(stepCount,current+delta));
    return snapshot();
  }
  function firstPending() {
    for (let order=1; order<=stepCount; order++)
      if (!completed.has(order)) return order;
    return null;
  }
  function jumpToFirstPending() {
    const pending=firstPending();
    if (pending!==null) current=pending;
    return snapshot();
  }
  function reset() { prepared.clear(); completed.clear(); current=stepCount?1:null; return snapshot(); }
  return {snapshot, markIngredient, markStep, move, firstPending, jumpToFirstPending, reset};
}

export function createManualTimer(now = () => performance.now()) {
  invariant(typeof now === "function", "Reloj inválido");
  let status="idle", remaining=0, deadline=null, lastTime=-Infinity;
  function time() {
    const value=now();
    invariant(Number.isFinite(value) && value>=lastTime, "Reloj no monótono");
    lastTime=value;
    return value;
  }
  function update(at) {
    if (status==="running") {
      remaining=Math.max(0,deadline-at);
      if (remaining===0) {status="finished"; deadline=null;}
    }
  }
  function view() {
    return {status, remainingMs:remaining, remainingSeconds:Math.ceil(remaining/1000)};
  }
  function snapshot() {update(time());return view();}
  function start(minutes, seconds) {
    invariant(Number.isInteger(minutes) && minutes>=0 && Number.isInteger(seconds) &&
      seconds>=0 && seconds<60 && minutes*60+seconds>0 && minutes*60+seconds<=MAX_SECONDS,
      "Duración inválida");
    const at=time();update(at);
    invariant(status==="idle" || status==="finished", "Temporizador ya activo");
    remaining=(minutes*60+seconds)*1000;deadline=at+remaining;status="running";
    return view();
  }
  function pause() {
    const at=time();update(at);
    if(status==="running"){status="paused";deadline=null;}
    return view();
  }
  function resume() {
    const at=time();
    if(status==="paused"){deadline=at+remaining;status="running";}
    update(at);return view();
  }
  function cancel(){status="idle";remaining=0;deadline=null;return view();}
  return {snapshot,start,pause,resume,cancel};
}
