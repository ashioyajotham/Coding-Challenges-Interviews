from collections import OrderedDict
import json
import os
import sys

assert sys.version_info >= (3, 2), (
    "This program requires Python 3.2+.  "
    "You're trying to run it with Python {}.".format(".".join(map(str, sys.version_info[:3]))))

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        sys.stderr.write("Usage: COMMAND <table-folder> <sql-json-file> <output-file>\n")
        sys.exit(1)
    table_folder, sql_json_file, output_file = args

    # Load the query JSON.
    try:
        query = load_json_from_file(sql_json_file)
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
        table = Table(raw_table[0], raw_table[1:], table_decl['name'], table_decl['source'])
        tables.append(table)

    evaluator = Evaluator(tables, query)
    result = evaluator.evaluate()

    # TODO: Actually evaluate query.
    # For now, just dump the input back out.
    with open(output_file, "w") as out:
        write_table(out, result)

class Evaluator:
    compareFunc = {
        "=": lambda x, y: x == y,
        "!=": lambda x, y: x!= y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
    }

    oppositeComparator = {
        "=": "!=",
        "!=": "=",
        ">": "<",
        ">=": "<=",
        "<": ">",
        "<=": ">=",
    }

    def __init__(self, tables, query):
        self.tables = tables
        self.query = query
        self.indexDict = {}

        self.result = None
        self.resultRows = []
        self.resultColumns = []

    def evaluate(self):
        self.computeTable()
        self.filterRows()

        self.selectColumns()

        self.result = Table(self.resultColumns, self.resultRows, None, None)
        return self.result


    def computeTable(self):
        assert self.tables is not None

        # maybe make another function?
        i = 0
        for table in self.tables:
            for column in table.getColumns():
                if table.getName() not in self.indexDict:
                    self.indexDict[table.getName()] = {}

                self.indexDict[table.getName()][column[0]] = i
                i += 1

        self.computeCrossProduct()

    def computeCrossProduct(self):
        columns = []
        rows = []

        for table in self.tables:
            columns.extend(table.getColumns())

        for i in range(len(self.tables)):
            newRows = self.tables[i].getRows()

            rows = self.computeCrossProductRows(rows, newRows)

        self.resultRows = rows
        self.resultColumns = columns

        return

    def computeCrossProductRows(self, rowsA, rowsB):
        if (len(rowsA) == 0):
            return rowsB
        
        if (len(rowsB) == 0):
            return rowsA

        rows = []

        for rowA in rowsA:
            for rowB in rowsB:
                rows += [rowA + rowB]
        
        return rows

    def filterRows(self):
        if self.query['where'] == []:
            return
        
        rows = []
        keepRows = set()

        for cond in self.query['where']:
            op = cond['op']

            left = cond['left']
            right = cond['right']

            if ('column' in left and 'column' in right):
                leftCol = self.getColumnIndex(left['column'])
                rightCol = self.getColumnIndex(right['column'])
                result = self.compareColumns(op, leftCol, rightCol)

            elif ('column' in left and 'literal' in right):
                col = self.getColumnIndex(left['column'])
                literal = right['literal']
                result = self.compareColumnWithLiteral(op, col, literal)
            
            elif ('literal' in left and 'column' in right):
                col = self.getColumnIndex(right['column'])
                literal = left['literal']
                result = self.compareLiteralWithColumn(op, col, literal)
            
            if not keepRows:
                keepRows = keepRows.union(set(result))
            else:
                keepRows = keepRows.intersection(set(result))

        for index in keepRows:
            rows += [self.resultRows[index]]

        self.resultRows = rows
        return

    def getColumnIndex(self, column):
        if (column['table'] is not None):
            return self.indexDict[column['table']][column['name']]
        
        index = self.getColumnIndexByColumnName(column['name'])

        return index

    def getColumnIndexByColumnName(self, name):
        i = 0
        for column in self.resultColumns:
            if column[0] == name:
                return i
            i += 1

            # check ambiguous

    def getTableNameByColumnName(self, columnName):
        for tableName in self.indexDict:
            if columnName in self.indexDict[tableName]:
                return tableName


    def compareColumns(self, op, columnA, columnB):
        result = []

        i = 0
        for row in self.resultRows:
            left = row[columnA]
            right = row[columnB]
            if (self.compareFunc[op](left, right)):
                result += [i]
            i += 1

        return result

    def compareColumnWithLiteral(self, op, column, literal):
        result = [] 
    
        i = 0
        for row in self.resultRows:
            left = row[column]
            
            if (self.compareFunc[op](left, literal)):
                result += [i]
            i += 1
        return result
    
    def compareLiteralWithColumn(self, op, column, literal):
        oppComp = self.oppositeComparator[op]

        return self.compareColumnWithLiteral(oppComp, column, literal)

    
    def selectColumns(self):
        columns = []
        rows = []
        columnIndices = []
        selects = self.query['select']

        for select in selects:
            colName = select['name']

            sourceColName = select['source']['name']
            sourceTableName = select['source']['table']

            if sourceTableName:
                sourceTable = self.getTableByName(sourceTableName)
                sourceCol = sourceTable.getColumnByName(sourceColName)

                # throw if sourceCol is None?
                colType = sourceCol[1]
            else:
                sourceTableName = self.getTableNameByColumnName(sourceColName)
                column = self.resultColumns[self.getColumnIndexByColumnName(sourceColName)]
                colType = column[1]

            columns += [[colName, colType]]

            index = self.indexDict[sourceTableName][sourceColName]
            columnIndices += [index]            
            
        for row in self.resultRows:
            rows.append([row[i] for i in columnIndices])

        self.resultColumns = columns
        self.resultRows = rows
        return

    def getTableByName(self, name):
        for table in self.tables:
            if table.getName() == name:
                return table

class Table:
    def __init__(self, columns, rows, name=None, source=None):
        self.columns = columns
        self.rows = rows
        self.name = name
        self.source = source

    def getColumns(self):
        return self.columns

    def getRows(self):
        return self.rows

    def getName(self):
        return self.name

    def getSource(self):
        return self.source

    def getColumnByName(self, name):
        for column in self.columns:
            if column[0] == name:
                return column

    def getColumnIndexByName(self, name):
        i = 0
        for column in self.columns:
            if column[0] == name:
                return i
            i += 1

class JsonFileLoadError(Exception):
    pass

def load_json_from_file(path):
    try:
        with open(path, "r", encoding="ascii") as f:
            # Use OrderedDict so that the field order from the input is preserved when writing
            # the dict back out.  Not necessary for correctness, but nice for readability.  We
            # wouldn't need this in Python 3.7+, where the standard dict preserves order.
            return json.load(f, object_pairs_hook=OrderedDict)
    except IOError as e:
        raise JsonFileLoadError("Error reading: {}".format(e))
    except ValueError as e:
        raise JsonFileLoadError("Invalid JSON: {}".format(e))

def write_table(out, table):
    out.write("[\n")
    out.write("    {}".format(json.dumps(table.columns, separators=(",", ":"))))
    for row in table.rows:
        out.write(",\n    {}".format(json.dumps(row, separators=(",", ":"))))
    out.write("\n]\n")

# For quoting strings in messages to the user.
def q(s):
    assert isinstance(s, str)
    return json.dumps(s)

if __name__ == "__main__":
    main()
