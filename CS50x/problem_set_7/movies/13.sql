SELECT name
FROM people
JOIN stars on stars.person_id = people.id
JOIN movies on stars.movie_id = movies.id
WHERE NOT people.name = 'Kevin Bacon' AND
    people.id IN (
    SELECT person_id
    FROM stars
    WHERE movie_id IN (
        SELECT movies.id
        FROM movies
        JOIN stars on stars.movie_id = movies.id
        JOIN people on stars.person_id = people.id
        WHERE people.name = 'Kevin Bacon' and people.birth = 1958
    )
)
