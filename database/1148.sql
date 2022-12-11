/* 1148 Article Views I */

/* Without subquery */
SELECT DISTINCT author_id AS id
FROM Views WHERE author_id = viewer_id
ORDER BY author_id;

/* Using subquery */
SELECT DISTINCT author_id AS id
FROM Views WHERE author_id
IN (SELECT viewer_id FROM Views WHERE author_id = viewer_id)
ORDER BY author_id;