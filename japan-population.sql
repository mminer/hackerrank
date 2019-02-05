-- Finds the total population of Japanese cities.
-- https://www.hackerrank.com/challenges/japan-population

SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN'
