-- Max temperature grouped by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
