-- Import the database dump from hbtn_0d_tvshows
SELECT
    s.title,
    g.genre_id
FROM
    tv_show_genres g
    RIGHT JOIN tv_shows s ON s.id = g.show_id
WHERE
    g.genre_id IS NULL
ORDER BY
s.title ASC,
g.genre_id ASC;
