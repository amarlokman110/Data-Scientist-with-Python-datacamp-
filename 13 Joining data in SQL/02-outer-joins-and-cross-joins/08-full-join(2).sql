/*
You'll now investigate a similar exercise to the last one, but this time focused on using a table with more records on the left than the right. You'll work with the languages and countries tables.

Begin with a full join with languages on the left and countries on the right. Appropriate fields have been selected for you again here.
*/

/*
Instructions 1/3
Choose records in which countries.name starts with the capital letter 'V' or is NULL.
Arrange by countries.name in ascending order to more clearly see the results.
*/
SELECT countries.name, code, languages.name AS language
FROM countries
FULL JOIN languages
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;

/*
Instructions 2/3
Repeat the same query as above but use a left join instead of a full join. Note what has changed compared to the full join result!
*/
SELECT countries.name, code, languages.name AS language
FROM languages
LEFT JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;

/*
Instructions 3/3
Repeat once more, but use an inner join instead of a left join. Note what has changed compared to the full join and left join results.
*/
SELECT countries.name, code, languages.name AS language
FROM languages
INNER JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;