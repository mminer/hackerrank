-- Sums the population of all countries in Asia.
-- https://www.hackerrank.com/challenges/asian-population

SELECT SUM(CITY.POPULATION)
FROM CITY, COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE
  AND CONTINENT = 'Asia'
