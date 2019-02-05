-- Calculates the average population of cities, rounded down.
-- https://www.hackerrank.com/challenges/average-population

SELECT FLOOR(AVG(POPULATION))
FROM CITY
