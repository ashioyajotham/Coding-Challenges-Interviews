-- Big cities in Japan
SELECT name, population
FROM cities
WHERE country = "Japan" AND population > 8000
