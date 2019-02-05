-- Finds the average population of cities in each continent.
-- https://www.hackerrank.com/challenges/average-population-of-each-continent

SELECT CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY, COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY CONTINENT
