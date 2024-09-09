-- List all genres of the show Dexter.
SELECT
    g.name
FROM
    tv_genres g
    LEFT JOIN tv_show_genres sg ON sg.genre_id = g.id
    LEFT JOIN tv_shows s ON s.id = sg.show_id
WHERE
    s.title = 'Dexter'
ORDER BY
    g.name
