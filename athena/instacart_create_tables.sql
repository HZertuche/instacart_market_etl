-- Top 10 most purchased products
SELECT product_name,
COUNT(*) AS total_products
FROM "instacart_market_db"."instacart_cleaned"
GROUP BY product_name
ORDER BY total_products DESC
limit 10;

-- Departments with the most orders
SELECT department, 
 COUNT(DISTINCT order_id) as total_orders
from instacart_cleaned
GROUP BY department
ORDER BY total_orders DESC;

-- Top 10 users with most orders
SELECT user_id,
COUNT (distinct order_number) AS user_orders
FROM "instacart_market_db"."instacart_cleaned" 
GROUP BY user_id
ORDER BY user_orders DESC
limit 10;

-- Verify the total orders from one top 10 user
SELECT user_id,
COUNT(*) AS user_orders,
order_number
FROM "instacart_market_db"."instacart_cleaned"
WHERE user_id = 86109
GROUP BY user_id, order_number
ORDER BY order_number ASC;

-- Weekday with the least orders
SELECT order_dow,
count (distinct order_id) as orders_by_day
FROM "instacart_market_db"."instacart_cleaned"
GROUP BY order_dow
ORDER BY orders_by_day asc;