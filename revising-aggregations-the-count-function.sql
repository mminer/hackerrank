-- Counts the number of cities with a population larger than 100,000.
-- https://www.hackerrank.com/challenges/revising-aggregations-the-count-function

SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000
