-- Can't refer to "cities.name" because the "cities" table is named "c".
SELECT cities.name
FROM cities AS c
WHERE population > 10
