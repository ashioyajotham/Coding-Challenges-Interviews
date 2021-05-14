# SQL Evaluator - Starter code for Scala 1.13

This includes code to parse the table and query JSON formats into Scala objects.

Look at "src/main/scala/sql_evaluator/Main.scala" to get started.

To build (requires sbt):

```
sbt build
```

To run directly:

```
./sql_evaluator ../../examples ../../examples/cities-2.sql.json out.txt
cat out.txt
```

To test against all the examples using the "check" tool:

```
../../check ./sql_evaluator -- ../../examples ../../examples/*.sql
```
