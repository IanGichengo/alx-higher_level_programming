-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title, SUM(rating) AS rating
FROM hbtn_0d_tvshows_rate
INNER JOIN tv_shows ON hbtn_0d_tvshows_rate.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY `rating sum` DESC;
