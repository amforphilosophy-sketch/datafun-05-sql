-- library_query_checkouts_by_branch.sql
-- Count checkouts and summarize fines for each branch.

SELECT
    b.branch_name,
    b.city,
    COUNT(c.checkout_id) AS checkout_count,
    SUM(c.fine_amount)   AS total_fines,
    AVG(c.fine_amount)   AS avg_fine
FROM branch AS b
JOIN checkout AS c
    ON b.branch_id = c.branch_id
GROUP BY b.branch_name, b.city
ORDER BY checkout_count DESC;
