/* 175 Combine Two Tables */

/* Using LEFT JOIN */
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a
ON p.personId = a.personId;