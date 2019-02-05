-- Lists all countries in Africa.
-- https://www.hackerrank.com/challenges/african-cities

SELECT CITY.NAME
FROM CITY, COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE
  AND CONTINENT = 'Africa'
