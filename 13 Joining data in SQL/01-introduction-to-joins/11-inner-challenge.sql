/*
The table you created with the added geosize_group field has been loaded for you here with the name countries_plus. Observe the use of (and the placement of) the INTO command to create this countries_plus table:

SELECT name, continent, code, surface_area,
    CASE WHEN surface_area > 2000000
            THEN 'large'
       WHEN surface_area > 350000
            THEN 'medium'
       ELSE 'small' END
       AS geosize_group
INTO countries_plus
FROM countries;
You will now explore the relationship between the size of a country in terms of surface area and in terms of population using grouping fields created with CASE.

By the end of this exercise, you'll be writing two queries back-to-back in a single script. You got this!
*/

/*
Instructions 1/3
Using the populations table focused only for the year 2015, create a new field AS popsize_group to organize population size into

'large' (> 50 million),
'medium' (> 1 million), and
'small' groups.
Select only the country code, population size, and this new popsize_group as fields.
*/
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
FROM populations
WHERE year = 2015;

/*
Instructions 2/3
Use INTO to save the result of the previous query as pop_plus. You can see an example of this in the countries_plus code in the assignment text. Make sure to include a ; at the end of your WHERE clause!

Then, include another query below your first query to display all the records in pop_plus using SELECT * FROM pop_plus; so that you generate results and this will display pop_plus in query result.
*/
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;

SELECT * FROM pop_plus;

/*
Instructions 3/3
Keep the first query intact that creates pop_plus using INTO.
Remove the SELECT * FROM pop_plus; code and instead write a second query to join countries_plus AS c on the left with pop_plus AS p on the right matching on the country code fields.
Select the name, continent, geosize_group, and popsize_group fields.
Sort the data based on geosize_group, in ascending order so that large appears on top.
*/
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;

SELECT c.name, c.continent, c.geosize_group, p.popsize_group
FROM countries_plus as c
INNER JOIN pop_plus as p
ON c.code = p.country_code
ORDER BY c.geosize_group