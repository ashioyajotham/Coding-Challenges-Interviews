-- "name" in the SELECT clause is ambiguous, because it is in more than one table.
-- To disambiguate, write "countries.name" or "cities.name", like in the WHERE clause.
SELECT name, country, population
FROM countries, cities
WHERE capital = cities.name
