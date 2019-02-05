-- Finds the difference between the maximum and minimum populations.
-- https://www.hackerrank.com/challenges/population-density-difference

SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY
