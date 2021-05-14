-- Cities that are more populous than their country's capital city.
SELECT others.name
FROM
    countries,
    cities AS capitals,
    cities AS others
WHERE
    countries.capital = capitals.name
    AND countries.name = others.country
    AND others.population > capitals.population
