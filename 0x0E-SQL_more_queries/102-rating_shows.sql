-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT T.title, (SELECT SUM(R.rate) FROM tv_show_ratings R WHERE T.id = R.show_id) AS rating
FROM tv_shows T
ORDER BY rating DESC;
