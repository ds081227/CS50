SELECT movies.title, ratings.rating
FROM movies
JOIN ratings on movies.id = ratings.movie_id
WHERE movies.year = 2010
ORDER BY rating DESC, title;
