SELECT
    g.name,
    COUNT(sg.show_id) as number_of_shows
FROM
    tv_genres g
    LEFT JOIN tv_show_genres sg ON sg.genre_id = g.id
GROUP BY
    g.name
ORDER BY
    number_of_shows DESC
