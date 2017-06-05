-- Queries names of all American cities with populations larger than 120000.
-- https://www.hackerrank.com/challenges/revising-the-select-query-2

SELECT NAME
FROM CITY
WHERE COUNTRYCODE = "USA" AND POPULATION > 120000
