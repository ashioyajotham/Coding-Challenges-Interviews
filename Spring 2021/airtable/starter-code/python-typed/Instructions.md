# SQL Evaluator - Starter code for Python 3.8+ (with static types)

To install Mypy and use it to type check:

```
python3 -m pip install mypy
python3 -m mypy .
```

To run:

```
python3 sql_evaluator.py ../../examples ../../examples/cities-2.sql.json out.txt
cat out.txt
```

To test against all the examples using the "check" tool:

```
../../check python3 sql_evaluator.py -- ../../examples ../../examples/*.sql
```
