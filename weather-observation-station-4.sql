-- Finds the difference between total entries and distinct ones.
-- https://www.hackerrank.com/challenges/weather-observation-station-4

SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION
