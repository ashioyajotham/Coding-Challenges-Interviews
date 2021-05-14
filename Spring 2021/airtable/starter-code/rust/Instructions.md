# SQL Evaluator - Starter code for Rust 1.40+

To build:

```
cargo build
```

To run:

```
./target/debug/sql_evaluator ../../examples ../../examples/cities-2.sql.json out.txt
cat out.txt
```

To test against all the examples using the "check" tool:

```
../../check ./target/debug/sql_evaluator -- ../../examples ../../examples/*.sql
```
