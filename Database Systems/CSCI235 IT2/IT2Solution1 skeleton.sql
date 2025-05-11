\set ECHO all
/* ====================================================== * 
 * Implementation Task 2                                  *
 * Student number: 12345678                               *
 * Name: Your name                                        *
 * ====================================================== */
--
-- Task 1
-- Query (i)
-- Implementation of Task 1 before creating of index
explain analyze
select l_discount
from lineitem
where l_shipdate = (select max(l_shipdate) from lineitem);
--
-- Query (ii)
--
-- Query (iii)
--
-- Query (iv)
--
-- Query (v)
--
-- Create the index
create index IT2Task1Idx on lineitem(attr1, attr2, attr3, attr4, ...);
--
-- Implementation of Task 1 after creating of index
explain analyze
select l_discount
from lineitem
where l_shipdate = (select max(l_shipdate) from lineitem);
--
-- Query (ii)
--
-- Query (iii)
--
-- Query (iv)
--
-- Query (v)
--
--
-- Drop the index when done
drop index IT2Task1Idx cascade;
--
\set ECHO none
