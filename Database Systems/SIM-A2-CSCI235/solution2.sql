-- Task 2: SUP_COST_REPORT Function
 CREATE OR REPLACE FUNCTION SUP_COST_REPORT(pPartKey PARTSUPP.ps_partkey%TYPE)
  RETURNS TEXT
 LANGUAGE plpgsql AS
 $$
 DECLARE
    cheapest RECORD;
    dearest  RECORD;
    result   TEXT;
 BEGIN
    SELECT s.s_suppkey, s.s_name, ps.ps_supplycost
      INTO cheapest
    FROM partsupp ps
    JOIN supplier s ON ps.ps_suppkey = s.s_suppkey
    WHERE ps.ps_partkey = pPartKey
    ORDER BY ps.ps_supplycost
    LIMIT 1;
    SELECT s.s_suppkey, s.s_name, ps.ps_supplycost
      INTO dearest
    FROM partsupp ps
    JOIN supplier s ON ps.ps_suppkey = s.s_suppkey
    WHERE ps.ps_partkey = pPartKey
    ORDER BY ps.ps_supplycost DESC
    LIMIT 1;
    result := format(
      'Supplier with cheapest cost: %s, %s, %s.'||
      'Supplier with dearest cost: %s, %s, %s.',
      cheapest.s_suppkey,
      TRIM(cheapest.s_name),
      TO_CHAR(cheapest.ps_supplycost,'FM$999,999,990.00'),
      dearest.s_suppkey,
      TRIM(dearest.s_name),
      TO_CHAR(dearest.ps_supplycost,'FM$999,999,990.00')
    );
    RETURN result;
 END;
 $$;-- Example calls:
 SELECT SUP_COST_REPORT(3753)  AS part_3753;
 SELECT SUP_COST_REPORT(43064) AS part_43064;
 SELECT SUP_COST_REPORT(57574) AS part_57574;
 SELECT SUP_COST_REPORT(60000) AS part_60000;
 
