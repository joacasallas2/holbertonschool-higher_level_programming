-- List all genres of the show Dexter.
SELECT
    g.name
FROM
    tv_genres g
    LEFT JOIN tv_show_genres sg ON sg.genre_id = g.id
WHERE
    sg.show_id = (
        SELECT
            s.id
        FROM
            tv_shows s
        WHERE
            s.title = 'Dexter'
    )
