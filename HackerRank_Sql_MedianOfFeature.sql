
-- Weather Observation Station 20
-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem

-- Description
-- A median is defined as a number separating the higher half of a data set from the lower half. 
-- Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.



-- Code

SELECT CAST(ROUND(AVG(LAT_N),4) AS NUMERIC(6,4))
FROM (
    SELECT  ROW_NUMBER() OVER (ORDER BY LAT_N) AS ranking, 
            LAT_N,
            ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS ranking_last
    FROM STATION
) x
WHERE ranking=ranking_last or (ranking-ranking_last)=1 or (ranking-ranking_last)=-1;
