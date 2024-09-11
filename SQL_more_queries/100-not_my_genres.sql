-- List all genres not linked to the show Dexter
SELECT
    g.name
FROM
    tv_genres g
WHERE
    g.name not in (
        SELECT
            g.name
        FROM
            tv_genres g
            INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
            INNER JOIN tv_shows s ON s.id = sg.show_id
        WHERE
            s.title = 'Dexter'
    )
GROUP BY
    g.name
