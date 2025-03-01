SELECT *
FROM inventory INNER JOIN rental ON rental.inventory_id = Inventory.inventory_id
LIMIT 5
