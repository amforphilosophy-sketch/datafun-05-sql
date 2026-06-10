-- library_query_checkouts_by_material.sql
-- Count checkouts and average loan duration for each material type.

SELECT
    material_type,
    COUNT(checkout_id)  AS checkout_count,
    AVG(duration_days)  AS avg_duration_days,
    SUM(fine_amount)    AS total_fines
FROM checkout
GROUP BY material_type
ORDER BY checkout_count DESC;
