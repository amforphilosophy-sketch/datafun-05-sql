-- library_query_kpi_system.sql
-- KPI: Total checkouts and fines rolled up by library system.

SELECT
    b.system_name,
    COUNT(c.checkout_id) AS checkout_count,
    SUM(c.fine_amount)   AS total_fines,
    AVG(c.fine_amount)   AS avg_fine
FROM branch AS b
JOIN checkout AS c
    ON b.branch_id = c.branch_id
GROUP BY b.system_name
ORDER BY checkout_count DESC;
