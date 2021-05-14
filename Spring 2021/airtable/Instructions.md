# Programming Assignment: SQL Evaluator

## Getting started

To develop locally (recommended):
1. Clone the git repo (click "Use local IDE (via Git)" in the top right corner).
2. Make changes to the starter code and test locally.
3. Push commits to the git remote.

To help keep our review process anonymous, please do not include any personally identifiable information (such as your name) in your submitted code.

## Assignment details

Write a command-line program that evaluates simple SQL queries.

Your program doesn't have to parse SQL directly.  We've provided a tool (`sql-to-json`) that converts [our subset of SQL](#simplified-sql) into a [JSON-based format](#json-formatted-sql) for your program to load.

```
$ ./YOUR-PROGRAM <table-folder> <sql-json-file> <output-file>
```

NOTE: In order to integrate with our scoring script YOUR-PROGRAM must be an executable file named `sql_evaluator`. The `sql_evaluator` file can either directly be your program executable or just a script that invokes your program (passing through commandline args as necessary). If it's a script ensure the proper [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) is set.

Your program should:
1. Load the [JSON-formatted SQL](#json-formatted-sql) file (".sql.json").
2. Load the [JSON-formatted tables](#json-formatted-table) referenced by the query.  For example, the table "countries" should be loaded from "\<table-folder\>/countries.table.json".
3. If there is an error in the query, write an error message to the output file and exit.  You only need to report the first error; you can stop processing the query after that.
4. If there are no errors, evaluate the query and write the result table to the output file.

You can assume the JSON-formatted SQL and table files are syntactically valid.  However, you should detect logical errors in the queries, such as:
- References to column names or table names that don't exist.
- Ambiguous column references (the column name exists in multiple tables).
- Use of a comparison operator on incompatible types (string vs integer).

You should perform the evaluation entirely in memory, using the standard data structures provided by your programming language.
- Avoid libraries that already implement a relational database, or a large subset of one; for example, do not use SQLite, Apache Derby, Pandas dataframes, etc.
- You can use external libraries to help with reading/writing JSON.
- We've provided starter code for several languages (see the "starter-code" folder), which you can use if you like.  Please include the starter code folder's "version.txt" in your submission.

Be sure to read over the [Evaluation Criteria](#evaluation-criteria) before submitting!

## How you should evaluate an SQL query

Let's run through one of the examples, "examples/simple-3.sql"

```sql
SELECT
    a1.name AS a1_name,
    a1.age,
    a2.name AS a2_name,
    b.distance
FROM
    a AS a1,
    a AS a2,
    b
WHERE
    distance > a2.age AND a1.name != "Bob"
```

Your program doesn't have to parse SQL directly.  We've provided a tool (`sql-to-json`) that converts [our subset of SQL](#simplified-sql) into a [JSON-based format](#json-formatted-sql) for your program to load.

```
$ ./sql-to-json examples/simple-3.sql  # writes to "examples/simple-3.sql.json"
```

(We've already pre-generated the ".sql.json" for all queries in the "examples" folder.  But if you want to create a new query or modify an existing one, you can write SQL and use `sql-to-json` to generate the JSON-formatted equivalent.)

```json
{
    "select": [
        {"name": "a1_name", "source": {"name": "name", "table": "a1"}},
        {"name": "age", "source": {"name": "age", "table": "a1"}},
        {"name": "a2_name", "source": {"name": "name", "table": "a2"}},
        {"name": "distance", "source": {"name": "distance", "table": "b"}}
    ],
    "from": [
        {"name": "a1", "source": "a"},
        {"name": "a2", "source": "a"},
        {"name": "b", "source": "b"}
    ],
    "where": [
        {
            "op": ">",
            "left": {"column": {"name": "distance", "table": null}},
            "right": {"column": {"name": "age", "table": "a2"}}
        },
        {
            "op": "!=",
            "left": {"column": {"name": "name", "table": "a1"}},
            "right": {"literal": "Bob"}
        }
    ]
}
```

Notice that all `select` and `from` entries have a `name`.  If the original SQL uses an `AS` clause, that is used as the `name`.  If not, `name` is automatically filled in based on the `source`.

To run your program on this example, we'd do:

```
$ YOUR-PROGRAM examples examples/simple-3.sql.json examples/simple-3.out
```

First, your program should load all the tables listed in the `FROM`.  (The provided starter code already does this.)

```javascript
// examples/a.table.json
[
    [["name", "str"], ["age", "int"]],
    ["Alice", 20],
    ["Bob", 30],
    ["Eve", 40]
]

// examples/b.table.json
[
    [["name", "str"], ["distance", "int"]],
    ["Q", 25],
    ["R", 32]
]
```

Before evaluating the query, validate it.  (This particular query does not have any errors, but see "examples/error-\*.sql" for examples of queries with errors.)

To evaluate the query, compute the cross-product (every combination of rows) of the tables in the `from` list:

```
|      a1     |      a2     |       b         |
| name  | age | name  | age | name | distance |
-----------------------------------------------
| Alice | 20  | Alice | 20  | Q    | 25       |
| Alice | 20  | Alice | 20  | R    | 32       |
| Alice | 20  | Bob   | 30  | Q    | 25       |
| Alice | 20  | Bob   | 30  | R    | 32       |
| Alice | 20  | Eve   | 40  | Q    | 25       |
| Alice | 20  | Eve   | 40  | R    | 32       |
| Bob   | 30  | Alice | 20  | Q    | 25       |
| Bob   | 30  | Alice | 20  | R    | 32       |
| Bob   | 30  | Bob   | 30  | Q    | 25       |
| Bob   | 30  | Bob   | 30  | R    | 32       |
| Bob   | 30  | Eve   | 40  | Q    | 25       |
| Bob   | 30  | Eve   | 40  | R    | 32       |
| Eve   | 40  | Alice | 20  | Q    | 25       |
| Eve   | 40  | Alice | 20  | R    | 32       |
| Eve   | 40  | Bob   | 30  | Q    | 25       |
| Eve   | 40  | Bob   | 30  | R    | 32       |
| Eve   | 40  | Eve   | 40  | Q    | 25       |
| Eve   | 40  | Eve   | 40  | R    | 32       |
```

Then, filter down to the rows that satisfy the `where` conditions:

```
|      a1     |      a2     |       b         |
| name  | age | name  | age | name | distance |
-----------------------------------------------
| Alice | 20  | Alice | 20  | Q    | 25       |
| Alice | 20  | Alice | 20  | R    | 32       |
| Alice | 20  | Bob   | 30  | R    | 32       |
| Eve   | 40  | Alice | 20  | Q    | 25       |
| Eve   | 40  | Alice | 20  | R    | 32       |
| Eve   | 40  | Bob   | 30  | R    | 32       |
```

Then, pull out the columns specified by the `SELECT`:

```
| a1_name | age | a2_name | distance |
--------------------------------------
| Alice   | 20  | Alice   | 25       |
| Alice   | 20  | Alice   | 32       |
| Alice   | 20  | Bob     | 32       |
| Eve     | 40  | Alice   | 25       |
| Eve     | 40  | Alice   | 32       |
| Eve     | 40  | Bob     | 32       |
```

Then, write the JSON-formatted results to the output file, "examples/simple-3.out":

```json
[
    [["a1_name", "str"], ["age", "int"], ["a2_name", "str"], ["distance", "int"]],
    ["Alice", 20, "Alice", 25],
    ["Alice", 20, "Alice", 32],
    ["Alice", 20, "Bob", 32],
    ["Eve", 40, "Alice", 25],
    ["Eve", 40, "Alice", 32],
    ["Eve", 40, "Bob", 32]
]
```

Once your program finishes running, make sure the output matches the ".expected" output file we've provided, "examples/simple-3.expected".
- The order of the columns matters.
- The order of the rows doesn't matter.
- The formatting doesn't matter as long as it's valid JSON.  (Our starter code knows how to write a table out with the same formatting as our examples.)

We've provided another tool (`check`) to automate these steps.  It will:
1. Convert the SQL file to a JSON-formatted SQL file.
2. Run your program.
3. Compare your program's output file to the expected output file.

```
$ ./check ./sql_evaluator -- <table-folder> <sql-files...>
```

To run against all the example queries:
```
$ ./check ./sql_evaluator -- examples examples/*.sql
```

## Evaluation Criteria

- **Above all else**, we're looking for clean code: correct, easy to understand, and easy to maintain.
- Stick to the overall structure of the cross-product technique outlined above.  Do not add optimizations like pre-filtering tables, pre-projecting columns, indexes, multi-threading, cross-product reordering, etc.
- Within the cross-product framework, the code should still be efficient.  Don't worry about profiling and measuring microseconds, but don't just throw away CPU or memory doing redundant work.
- Assume that the normal use case involves loading the tables once and then evaluating many different queries.  (Your program doesn't _actually_ do this, but use this model when thinking about efficiency.)

To allow focusing on the above priorities, we're explicitly excluding a few things from the evaluation criteria:
- Feel free to write any tests you need to gain confidence in your code, but we won't be looking at them at all.
- Don't worry about extensibility beyond the requirements given here.  For example, don't worry about handling other SQL features, other SQL data types, non-read-only tables, etc.
- We care about how your code is decomposed into functions and classes, but all your validation and evaluation code can be in one file, if that makes things easier.

When you submit your code, **you must include a ReadMe text file** with:
- Instructions on how to run your code.
- A brief explanation of any interesting choices you made in the design or implementation.

## Submitting assignment

1. Make sure all of your changes are pushed to the git remote.
2. Press the "Submit" button which will take you to the questions overview page.
3. Press the "Submit Test" button.

**Your code does NOT need to run in the HackerRank environment (e.g. using the "Run Tests" button).**

If you have issues submitting through HackerRank you can email your recruiter a `.zip` of your submission.

NOTE: The following files are READ ONLY and should not be edited. The upstream git remote will reject any commits with changes to these files, so make sure they are not modified in any commits.
- hackerrank.yml
- score.sh
- version.txt
- Instructions.html
- Instructions.md
- check
- sql-to-json
- examples/*.json
- examples/*.expected
- examples/*.sql

## File Formats

### Simplified SQL

(You don't have to write a parser for this syntax.  The included `sql-to-json` tool will convert this syntax to a JSON-formatted equivalent.)

```
Query =
    "SELECT" Selector ( "," Selector )*
    "FROM" TableDecl ( "," TableDecl )*
    ( "WHERE" Comparison ( "AND" Comparison )* )?

Selector = ColumnRef ( "AS" <identifier> )?

TableDecl = <identifier> ( "AS" <identifier> )?

Comparison = Term ( "=" | "!=" | ">" | ">=" | "<" | "<=" ) Term

Term = ColumnRef | <string-literal> | <integer-literal>

ColumnRef = <identifier> ( "." <identifier> )?
```

Comments start with "--" and go to the end of the line.

Joins are performed using [implicit cross-join notation](https://en.wikipedia.org/wiki/Join_(SQL)#Inner_join).

### JSON-formatted SQL

```
Query = {
    select: Array<Selector>  // non-empty array
    from: Array<TableDecl>  // non-empty array
    where: Array<Comparison>
}

Selector = {
    name: string  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: ColumnRef
}

TableDecl = {
    name: string  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: string  // the file to load (without the ".table.json" extension)
}

Comparison = {
    op: "=" | "!=" | ">" | ">=" | "<" | "<="
    left: Term
    right: Term
}

Term = {column: ColumnRef} | {literal: int | string}

ColumnRef = {
    name: string
    table: string | null  // non-null for fully-qualified ColumnRefs ("table1.column2")
}
```

### JSON-formatted Table

Each ".table.json" file is a JSON array.  The first element is a list of column definitions.  Each column definition is a pair where the first element is the column name and the second element is the column type (either "str" or "int").

The rest of the elements are the table's rows.  Each cell value will be either a string or an integer, depending on the columnn type.
