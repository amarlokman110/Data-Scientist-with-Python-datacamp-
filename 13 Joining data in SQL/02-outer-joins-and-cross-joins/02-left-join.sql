/*
Now you'll explore the differences between performing an inner join and a left join using the cities and countries tables.

You'll begin by performing an inner join with the cities table on the left and the countries table on the right. Remember to alias the name of the city field as city and the name of the country field as country.

You will then change the query to a left join. Take note of how many records are in each query here!
*/

/*
Instructions
- Fill in the code shown to complete the inner join. Note how many records are in the result of the join in the query result tab.
- Change the code to perform a LEFT JOIN instead of an INNER JOIN. After executing this query, note how many records the query result contains.
*/

-- get the city name (and alias it), the country code,
-- the country name (and alias it), the region,
-- and the city proper population
SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
-- specify left table
FROM cities AS c1
-- specify right table and type of join
INNER JOIN countries AS c2
-- how should the tables be matched?
ON c1.country_code = c2.code
-- sort based on descending country code
ORDER BY code DESC;

-- get the city name (and alias it), the country code,
-- the country name (and alias it), the region,
-- and the city proper population
SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
-- specify left table
FROM cities AS c1
-- specify right table and type of join
LEFT JOIN countries AS c2
-- how should the tables be matched?
ON c1.country_code = c2.code
-- sort based on descending country code
ORDER BY code DESC;