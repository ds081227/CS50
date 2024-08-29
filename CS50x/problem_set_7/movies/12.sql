SELECT title
FROM movies
JOIN stars on stars.movie_id = movies.id
JOIN people on stars.person_id = people.id
WHERE people.name = 'Jennifer Lawrence'

INTERSECT

SELECT title
FROM movies
JOIN stars on stars.movie_id = movies.id
JOIN people on stars.person_id = people.id
WHERE people.name = 'Bradley Cooper'

