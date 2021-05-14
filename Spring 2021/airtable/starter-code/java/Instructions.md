# SQL Evaluator - Starter code for Java 8+

This includes code to parse the table and query JSON formats into Java objects (using the [Jackson](https://github.com/FasterXML/jackson) library).

Look at "src/sql_evaluator/Main.java" to get started.

To build (requires Maven):

```
mvn compile
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
