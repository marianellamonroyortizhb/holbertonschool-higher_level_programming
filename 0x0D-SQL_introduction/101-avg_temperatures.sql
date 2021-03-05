-- Displays the average temperature by city ordered by descending.
SELECT city, AVG(score) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
