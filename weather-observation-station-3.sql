-- Queries a list of city names with even IDs.
-- https://www.hackerrank.com/challenges/weather-observation-station-3

SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0
