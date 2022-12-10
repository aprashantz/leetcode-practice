/* 1484 Group Sold Products By The Date */
SELECT sell_date, COUNT(DISTINCT product) AS num_sold,
group_concat(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date;