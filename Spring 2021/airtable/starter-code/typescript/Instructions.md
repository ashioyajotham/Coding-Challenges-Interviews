# SQL Evaluator - Starter code for Node 8+

To fetch dependencies and build:

```
npm install
npm build   # compiles once
npm watch   # keep recompiling whenever the Typescript code changes
```

To run:

```
node build/main.js ../../examples ../../examples/cities-2.sql.json out.txt
cat out.txt
```

To test against all the examples using the "check" tool:

```
../../check node build/main.js -- ../../examples ../../examples/*.sql
```
