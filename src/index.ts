import * as fs from 'fs';
import { parseHighlightsFromKindleExport } from "./kindle"
import { Notion } from "./notion"

function getFileFromArgs(args: string[]): string {
    let body = JSON.parse(args[0]);

    let b = Buffer.from(body["html"], 'base64');

    return b.toString('ascii')
}

function main() {
    const args = process.argv.slice(2);

    let file = (args.length == 0) ? fs.readFileSync('./input.html', 'utf8') : getFileFromArgs(args)
    const bookHighlights = parseHighlightsFromKindleExport(file)
    const notion = new Notion
    notion.writeHighlightsToNotion(bookHighlights)
}

main()