/* 1965 Employees With Missing Information */

/* Using UNION and LEFT JOIN */
SELECT e.employee_id FROM Employees e
LEFT JOIN Salaries s
ON e.employee_id = s.employee_id
WHERE s.employee_id IS null
UNION
SELECT s.employee_id FROM Salaries s
LEFT JOIN Employees e
ON s.employee_id = e.employee_id
WHERE e.employee_id IS null
ORDER BY employee_id;

