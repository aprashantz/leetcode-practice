/* 607 Sales Person */

/* Using Subquery */
SELECT name FROM SalesPerson WHERE sales_id NOT IN
(SELECT sales_id FROM Orders WHERE com_id NOT IN
(SELECT com_id FROM Company WHERE name != "RED"));

/* Using LEFT JOIN and Subquery */
SELECT name FROM SalesPerson s WHERE sales_id NOT IN
(SELECT o.sales_id FROM Orders o LEFT JOIN Company c
ON o.com_id = c.com_id WHERE c.name = 'RED');