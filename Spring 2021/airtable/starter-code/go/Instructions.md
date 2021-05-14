# SQL Evaluator - Starter code for Go 1.14+

This includes starter code to parse the table and query JSON formats into Go structs.

Although we try to write idiomatic Go, this code is intentionally bare-bones in order to avoid imposing a particular programming style on you. Free to modify it as much as you like to make your life easier.

To build:

```
go build ./cmd/sql_evaluator
```

To run directly:

```
./sql_evaluator ../../examples ../../examples/cities-2.sql.json out.txt
cat out.txt
```

To check against all the examples using the "check" tool:

```
../../check ./sql_evaluator -- ../../examples ../../examples/*.sql
```
