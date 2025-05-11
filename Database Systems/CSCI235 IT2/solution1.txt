-- Enable echo to show all SQL commands
\set ECHO all

-- =====================================
-- QUERY i: Discounts of most recently shipped items
-- =====================================
EXPLAIN ANALYZE
SELECT l_discount
FROM lineitem
WHERE l_shipdate = (SELECT MAX(l_shipdate) FROM lineitem);

-- =====================================
-- QUERY ii: Total items shipped by air in 1998
-- =====================================
EXPLAIN ANALYZE
SELECT COUNT(*) AS total_items
FROM lineitem
WHERE l_shipmode = 'AIR'
  AND l_shipdate BETWEEN DATE '1998-01-01' AND DATE '1998-12-31';

-- =====================================
-- QUERY iii: Order key & line number of highest discount
-- =====================================
EXPLAIN ANALYZE
SELECT l_orderkey, l_linenumber
FROM lineitem
WHERE l_discount = (SELECT MAX(l_discount) FROM lineitem);

-- =====================================
-- QUERY iv: Total items per line status
-- =====================================
EXPLAIN ANALYZE
SELECT l_linestatus, COUNT(*) AS total_items
FROM lineitem
GROUP BY l_linestatus;

-- =====================================
-- QUERY v: Specific order details
-- =====================================
EXPLAIN ANALYZE
SELECT l_orderkey, l_linenumber, l_linestatus, l_shipdate, l_shipmode
FROM lineitem
WHERE l_orderkey IN (1795718, 1799046, 1794626);

-- =====================================
-- INDEX CREATION SECTION
-- Optimized minimal set of indexes
-- =====================================
-- Index for filtering and max shipdate (Q1, Q2, Q5)
CREATE INDEX idx_shipdate ON lineitem(l_shipdate);

-- Index for filtering by shipping mode (Q2, Q5)
CREATE INDEX idx_shipmode ON lineitem(l_shipmode);

-- Index for highest discount (Q1, Q3)
CREATE INDEX idx_discount ON lineitem(l_discount);

-- Index for group by line status (Q4, Q5)
CREATE INDEX idx_linestatus ON lineitem(l_linestatus);

-- Index for specific order lookups (Q3, Q5)
CREATE INDEX idx_orderkey_linenumber ON lineitem(l_orderkey, l_linenumber);

-- =====================================
-- CLEANUP SECTION: Drop indexes after use
-- =====================================
DROP INDEX IF EXISTS idx_shipdate CASCADE;
DROP INDEX IF EXISTS idx_shipmode CASCADE;
DROP INDEX IF EXISTS idx_discount CASCADE;
DROP INDEX IF EXISTS idx_linestatus CASCADE;
DROP INDEX IF EXISTS idx_orderkey_linenumber CASCADE;

-- Disable echo if needed
\set ECHO none
