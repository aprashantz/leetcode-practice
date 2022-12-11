/* 608 Tree Node */

/* Using IF(), Without using UNION */
SELECT id,
IF(p_id IS null, "Root",
IF(id IN (SELECT p_id FROM Tree), "Inner", "Leaf"
)) AS type
FROM Tree;


/* Using UNION and WHERE */
SELECT id, 'Root' AS type
FROM Tree
WHERE p_id IS null
UNION
SELECT id, 'Inner' AS type
FROM Tree
WHERE id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT null)
    AND p_id IS NOT null
UNION
SELECT id, 'Leaf' AS type
FROM Tree
WHERE id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT null)
    AND p_id IS NOT null