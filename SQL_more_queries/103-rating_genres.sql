-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT
    g.name,
    SUM(rate) as rating
FROM
    tv_show_genres sg
    LEFT JOIN tv_show_ratings sr ON sr.show_id = sg.show_id
    LEFT JOIN tv_genres g ON g.id = sg.genre_id
    LEFT JOIN tv_shows s ON s.id = sg.show_id
GROUP BY
    sg.genre_id
ORDER BY
    rating DESC
