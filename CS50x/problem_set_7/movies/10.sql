SELECT DISTINCT name
FROM people
JOIN directors on people.id = directors.person_id
JOIN movies on directors.movie_id = movies.id
JOIN ratings on directors.movie_id = ratings.movie_id
WHERE ratings.rating >= 9.0
LIMIT 10;
