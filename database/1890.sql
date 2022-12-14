/* 1890 The Latest Login in 2020 */

/* Fast and easy */
SELECT user_id, MAX(time_stamp) AS 'last_stamp'
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;

/* Slower, using subquery */
SELECT user_id, MAX(time_stamp) AS 'last_stamp'
FROM LOGINS
WHERE (user_id, time_stamp) IN
(SELECT user_id, time_stamp
FROM Logins
WHERE YEAR(time_stamp) = '2020')
GROUP BY user_id;

