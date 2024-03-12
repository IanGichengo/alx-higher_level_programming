-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, AVG((temperature * 9/5) + 32) AS avg_temperature_f FROM temperatures GROUP BY city ORDER BY avg_temperature_f DESC;
