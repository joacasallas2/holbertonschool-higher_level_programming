-- Import in hbtn_0c_0 database a table dump
SELECT
    city,
    AVG(value) as avg_temp
FROM 
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp DESC
