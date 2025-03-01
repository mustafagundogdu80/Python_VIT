SELECT film.film_id, film.title, inventory.inventory_id
FROM film
	INNER JOIN Inventory ON Inventory.film_id = film.film_id 
