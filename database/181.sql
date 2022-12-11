/* 181 Employees Earning More Than Their Managers */

/* Using subquery (SLOW) */
SELECT name AS Employee
FROM Employee e WHERE
salary > (SELECT salary FROM Employee WHERE id = e.managerId);

/* Combining tables with WHERE */
SELECT e.name AS Employee
FROM Employee e, Employee m
WHERE
e.managerId = m.id AND
e.salary > m.salary

/* Using self join */
SELECT e.name AS Employee
FROM Employee e JOIN Employee m
ON e.managerId = m.id
AND e.salary > m.salary