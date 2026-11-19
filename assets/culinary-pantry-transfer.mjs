/* Traspaso de menciones, de un solo uso, en la misma pestaña. */
export const TRANSFER_KEY="novacoquinaria.pantry.mentions";
function validate(terms){
  if(!Array.isArray(terms)||terms.length<1||terms.length>2000||
     terms.some(t=>typeof t!=="string"||t.length>160||t.trim()!==t||
       /[\u0000-\u001f\u007f]/u.test(t)||!/[\p{L}\p{N}]/u.test(t)))
    throw Error("Selección de menciones inválida.");
  return [...terms];
}
export function putMentions(getStorage,terms){
  const value=JSON.stringify({version:"0.1.0",terms:validate(terms)});
  try{getStorage().setItem(TRANSFER_KEY,value);}
  catch{throw Error("No se pudo transferir la selección en esta pestaña.");}
}
export function takeMentions(getStorage){
  const storage=getStorage(),raw=storage.getItem(TRANSFER_KEY);
  if(raw===null)return null;
  storage.removeItem(TRANSFER_KEY);
  if(typeof raw!=="string"||raw.length>2000000)throw Error("Selección inválida.");
  const data=JSON.parse(raw);
  if(data?.version!=="0.1.0")throw Error("Formato de selección incompatible.");
  return validate(data.terms);
}
