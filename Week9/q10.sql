SELECT count(*)
FROM film
Where film_id is not null and
	title is not null and
	description is not null and
	release_year is not null and
	language_id is not null and
	rental_duration is not null and
	rental_rate is not null and
	film.length is not null and
	replacement_cost is not null and
	rating is not null and
	last_update is not null and
	special_features is not null and
	fulltext is not null 