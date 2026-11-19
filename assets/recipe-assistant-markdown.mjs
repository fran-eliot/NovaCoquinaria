/* Presentación conservadora del Markdown culinario: solo nodos DOM, nunca HTML de entrada. */
function el(tag, text) {
  const n=document.createElement(tag);
  if(text!==undefined)n.textContent=text;
  return n;
}
export function inline(target, value) {
  const text=String(value);
  const pattern=/(!?)\[([^\]\n]+)\]\(([^)\n]+)\)|(\*\*|__)(.+?)\4|(\*|_)([^*_\n]+)\6|`([^`\n]+)`/g;
  let last=0;
  for(const m of text.matchAll(pattern)){
    target.append(document.createTextNode(text.slice(last,m.index)));
    if(m[2]!==undefined)target.append(document.createTextNode(m[2]));
    else if(m[5]!==undefined)target.append(el("strong",m[5]));
    else if(m[7]!==undefined)target.append(el("em",m[7]));
    else target.append(el("code",m[8]));
    last=m.index+m[0].length;
  }
  target.append(document.createTextNode(text.slice(last)));
  return target;
}
export function renderMarkdown(target, value) {
  const lines=String(value).split(/\r?\n/);
  const fragment=document.createDocumentFragment();
  const heading=/^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$/;
  const list=/^(\s*)([-+*]|\d+[.)])\s+(.+)$/;
  const fence=/^\s{0,3}(```+|~~~+)/;
  const rule=/^\s*(?:-{3,}|\*{3,}|_{3,})\s*$/;
  const cells=s=>s.trim().replace(/^\||\|$/g,"").split("|").map(x=>x.trim());
  const tableStart=i=>i+1<lines.length&&lines[i].trim().startsWith("|")&&
    lines[i+1].trim().startsWith("|")&&cells(lines[i+1]).every(x=>/^:?-{3,}:?$/.test(x));
  let i=0;
  while(i<lines.length){
    const line=lines[i];
    if(!line.trim()){i++;continue;}
    const f=line.match(fence);
    if(f){const body=[line];i++;while(i<lines.length){const s=lines[i++];body.push(s);if(s.trim().startsWith(f[1]))break;}fragment.append(el("pre",body.join("\n")));continue;}
    const h=line.match(heading);
    if(h){fragment.append(inline(el("h"+Math.min(6,h[1].length+2)),h[2]));i++;continue;}
    if(rule.test(line)){fragment.append(el("hr"));i++;continue;}
    if(tableStart(i)){
      const wrap=el("div");wrap.className="table-scroll";
      const table=el("table"), head=el("thead"), row=el("tr");
      for(const cell of cells(line)){const th=inline(el("th"),cell);th.scope="col";row.append(th);}
      head.append(row);table.append(head);i+=2;
      const body=el("tbody");
      while(i<lines.length&&lines[i].trim().startsWith("|")){
        const tr=el("tr");for(const cell of cells(lines[i++]))tr.append(inline(el("td"),cell));body.append(tr);
      }
      table.append(body);wrap.append(table);fragment.append(wrap);continue;
    }
    const item=line.match(list);
    if(item){
      const ordered=/^\d/.test(item[2]), ul=el(ordered?"ol":"ul");
      if(ordered)ul.start=parseInt(item[2],10);
      while(i<lines.length){
        const m=lines[i].match(list);
        if(!m||/^\d/.test(m[2])!==ordered||m[1]!==item[1])break;
        const li=inline(el("li"),m[3]);ul.append(li);i++;
      }
      fragment.append(ul);continue;
    }
    const p=el("p");inline(p,line);fragment.append(p);i++;
  }
  target.replaceChildren(fragment);
}
