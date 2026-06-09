-- sql/duckdb/mohmand_retail_query_kpi_region.sql
-- ============================================================
-- KPI: Total Revenue by Region
-- ============================================================
-- Author: Ahmad Saleem Mohmand
--
-- KPI QUESTION:
-- "How much revenue did each region generate?"
--
-- This is a variation of the Total Revenue by Store KPI.
-- Instead of grouping at the store level, we roll the numbers
-- up to the region level so decision-makers can compare the
-- overall performance of each region at a glance.
--
-- STRATEGY:
-- - JOIN store (1) to sale (M) on store_id
-- - GROUP BY region
-- - SUM amounts to compute revenue per region
-- - ORDER results so the top region appears first
--
SELECT
  s.region,
  COUNT(sa.sale_id) AS sale_count,
  ROUND(SUM(sa.amount), 2) AS total_revenue,
  ROUND(AVG(sa.amount), 2) AS avg_sale_amount
FROM store AS s
JOIN sale AS sa
  ON sa.store_id = s.store_id
GROUP BY
  s.region
ORDER BY total_revenue DESC;
