# Write your MySQL query statement below
SELECT DISTINCT w.Id
FROM Weather w, Weather x
WHERE w.Temperature > x.Temperature
AND DATEDIFF(w.Recorddate, x.Recorddate) = 1