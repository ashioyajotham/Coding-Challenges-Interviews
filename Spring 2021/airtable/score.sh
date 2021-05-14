#!/usr/bin/env bash

# Just in case it's not already executable.
chmod u+x sql_evaluator

# Run against all test cases.
./check ./sql_evaluator -- examples examples/*.sql

if [ $? -eq 0 ]; then
    echo ""
    echo "All test cases passed!"
    echo "FS_SCORE:100%"
else
    echo ""
    echo "Some test cases failed; see output above."
    echo "FS_SCORE:0%"
fi
