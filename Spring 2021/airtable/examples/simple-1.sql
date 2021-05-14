SELECT
    a.name AS a_name,
    age,
    b.name AS b_name,
    distance
FROM
    a,  -- load from "a.table.json"
    b   -- load from "b.table.json"
