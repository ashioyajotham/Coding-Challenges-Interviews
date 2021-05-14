import {Query} from './model';
import {Table} from './table';

import * as fs from 'fs';
import * as path from 'path';

function main(): void {
    const args = process.argv.slice(2);
    if (args.length !== 3) {
        console.error("Usage: COMMAND <table-folder> <sql-json-file> <output-file>");
        throw process.exit(1);
    }

    const [tableFolder, sqlJsonFile, outputFile] = args;

    // Load the query JSON.
    const query: Query = loadJsonFromFile(sqlJsonFile);

    // Load all the tables referenced in the "FROM" clause.
    const tables: Array<Table> = [];
    for (const tableDecl of query.from) {
        const tableSourcePath = path.join(tableFolder, `${tableDecl.source}.table.json`);
        const rawTable = loadJsonFromFile(tableSourcePath);
        const table = new Table(rawTable[0], rawTable.slice(1));
        tables.push(table);
    }

    // TODO: Actually evaluate query.
    // For now, just dump the input back out.
    const outFd = fs.openSync(outputFile, 'w');
    try {
        fs.writeSync(outFd, JSON.stringify(query, null, 4));
        fs.writeSync(outFd, '\n');

        for (const table of tables) {
            writeTable(outFd, table);
        }
    } finally {
        fs.closeSync(outFd);
    }
}

function writeTable(outFd: number, table: Table): void {
    fs.writeSync(outFd, "[\n");
    fs.writeSync(outFd, `    ${JSON.stringify(table.columns)}`);
    for (const row of table.rows) {
        fs.writeSync(outFd, `,\n    ${JSON.stringify(row)}`);
    }
    fs.writeSync(outFd, "\n]\n");
}

function loadJsonFromFile(path: string): any {
    const contents = fs.readFileSync(path, {encoding: 'ascii'});
    return JSON.parse(contents);
}

if (require.main === module) {
    require('source-map-support').install();  // So stack traces refer to the original TypeScript line.
    main();
}
