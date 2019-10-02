/*
Why does the following code result in an error?

SELECT c.name AS country, l.name AS language
FROM countries AS c
INNER JOIN languages AS l;
*/

INNER JOIN requires a specification of the key field (or fields) in each table.