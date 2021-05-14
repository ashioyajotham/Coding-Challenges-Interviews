-- Type mismatch: "name" is a str and "population" is an int.
-- Comparisons only work between values of the same type.
SELECT name
FROM cities
WHERE country = "USA" AND name != population
