-- Sums the populations of cities in California.
-- https://www.hackerrank.com/challenges/revising-aggregations-sum

SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'
