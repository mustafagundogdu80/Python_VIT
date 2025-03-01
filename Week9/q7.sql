SELECT rental.rental_id, rental_date, payment_id
FROM Payment INNER JOIN rental ON rental.rental_id = Payment.rental_id
ORDER BY amount DESC
LIMIT 10
