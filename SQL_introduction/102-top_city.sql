-- displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)
SELECT
    city,
    AVG(value) as avg_temp
FROM
    temperatures
WHERE
    month = 7 or month = 8
GROUP by
    city
ORDER by
    avg_temp DESC
LIMIT 
    3
