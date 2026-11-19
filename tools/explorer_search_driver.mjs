import fs from "node:fs";
import { createSearch } from "../assets/culinary-explorer-search.mjs";

const catalog = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const requests = JSON.parse(fs.readFileSync(0, "utf8"));
const engine = createSearch(catalog);
const results = requests.map(request => {
  try {
    if (request.lexical !== undefined) return {key: engine.key(request.lexical), tokens: engine.tokens(request.lexical)};
    return {rows: engine.search(request).map(({recipe, matches}) => ({
      id: recipe.id,
      matches: matches.map(m => m.occurrences.map(({position, name, raw, optionality, source_location}) =>
        ({position, name, raw, optionality, source_location})))
    }))};
  } catch (error) { return {error: true}; }
});
process.stdout.write(JSON.stringify(results));
