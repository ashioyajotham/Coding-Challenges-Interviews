from __future__ import annotations

from typing import Any, List, TextIO

from model import ColumnDef, SqlValue, Query

import json
import os
import sys

assert sys.version_info >= (3, 8), (
    "This program requires Python 3.8+.  "
    "You're trying to run it with Python {}.".format(".".join(map(str, sys.version_info[:3]))))

def main() -> None:
    args = sys.argv[1:]
    if len(args) != 3:
        sys.stderr.write("Usage: COMMAND <table-folder> <sql-json-file> <output-file>\n")
        sys.exit(1)
    table_folder, sql_json_file, output_file = args

    # Load the query JSON.
    try:
        query: Query = load_json_from_file(sql_json_file)
    except JsonFileLoadError as e:
        sys.stderr.write("Error loading SQL JSON from {}: {}\n".format(q(sql_json_file), e))
        sys.exit(1)

    # Load all tables referenced in the "FROM" clause.
    tables = []
    for table_decl in query["from"]:
        table_source_path = os.path.join(table_folder, "{}.table.json".format(table_decl["source"]))
        try:
            raw_table = load_json_from_file(table_source_path)
        except JsonFileLoadError as e:
            sys.stderr.write("Error loading table JSON from {}: {}\n".format(q(table_source_path), e))
            sys.exit(1)
        table = Table(raw_table[0], raw_table[1:])
        tables.append(table)

    # TODO: Actually evaluate query.
    # For now, just dump the input back out.
    with open(output_file, "w") as out:
        json.dump(query, out, indent=4)
        out.write("\n")

        for table in tables:
            write_table(out, table)

class Table:
    columns: List[ColumnDef]
    rows: List[List[SqlValue]]

    def __init__(self, columns: List[ColumnDef], rows: List[List[SqlValue]]):
        self.columns = columns
        self.rows = rows

class JsonFileLoadError(Exception):
    pass

def load_json_from_file(path: str) -> Any:
    try:
        with open(path, "r", encoding="ascii") as f:
            return json.load(f)
    except IOError as e:
        raise JsonFileLoadError("Error reading: {}".format(e))
    except ValueError as e:
        raise JsonFileLoadError("Invalid JSON: {}".format(e))

def write_table(out: TextIO, table: Table) -> None:
    out.write("[\n")
    out.write("    {}".format(json.dumps(table.columns, separators=(",", ":"))))
    for row in table.rows:
        out.write(",\n    {}".format(json.dumps(row, separators=(",", ":"))))
    out.write("\n]\n")

# For quoting strings in messages to the user
def q(s: str) -> str:
    return json.dumps(s)

if __name__ == "__main__":
    main()
