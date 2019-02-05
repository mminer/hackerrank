-- Calculates the average population of cities in California.
-- https://www.hackerrank.com/challenges/revising-aggregations-sum

SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'
