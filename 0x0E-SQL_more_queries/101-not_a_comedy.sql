-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
) AS linked_shows ON tv_shows.id = linked_shows.show_id
WHERE linked_shows.show_id IS NULL
ORDER BY tv_shows.title;
