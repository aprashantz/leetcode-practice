/* 1729 Find Followers Count */
SELECT user_id, COUNT(user_id) AS 'followers_count'
FROM Followers
GROUP BY user_id
ORDER BY user_id;