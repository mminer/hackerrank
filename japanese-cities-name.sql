-- Query names of all Japanese cities.
-- https://www.hackerrank.com/challenges/japanese-cities-name

SELECT NAME
FROM CITY
WHERE COUNTRYCODE = "JPN"
