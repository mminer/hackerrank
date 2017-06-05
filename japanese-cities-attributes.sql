-- Queries all attributes of every Japanese city.
-- https://www.hackerrank.com/challenges/japanese-cities-attributes

SELECT *
FROM CITY
WHERE COUNTRYCODE = "JPN"
