import * as fs from 'fs';
import { parseHighlightsFromKindleExport } from "./kindle"
import { Notion } from "./notion"

const file = fs.readFileSync('./test.html', 'utf8');

const bookHighlights = parseHighlightsFromKindleExport(file)
const notion = new Notion
notion.writeHighlightsToNotion(bookHighlights)
