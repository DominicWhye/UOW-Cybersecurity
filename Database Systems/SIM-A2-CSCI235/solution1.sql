-- Task 1: SUPPLIERACCBAL Procedure
 CREATE OR REPLACE PROCEDURE SUPPLIERACCBAL (
  pRegion REGION.r_regionkey%TYPE
 )
 LANGUAGE plpgsql AS
 $SUPPLIERACCBAL$
 DECLARE
  curNationAvgAccBal  SUPPLIER.s_acctbal%TYPE := 0;
  curNationName       NATION.n_name%TYPE     := '';
  curSuppAcctBal      SUPPLIER.s_acctbal%TYPE := 0;
  aComment            TEXT                   := '';
  suppCursor          RECORD;
 BEGIN
  FOR suppCursor IN
    SELECT 
      s.s_name,
      s.s_phone,
      s.s_acctbal,
      n.n_name,
      s.s_nationkey
    FROM supplier s
    JOIN nation   n ON s.s_nationkey = n.n_nationkey
    JOIN region   r ON n.n_regionkey  = r.r_regionkey
    WHERE r.r_regionkey = pRegion
    ORDER BY n.n_name, s.s_name
  LOOP
    IF suppCursor.n_name <> curNationName THEN
      curNationName := suppCursor.n_name;
      RAISE NOTICE 'Nation: %', curNationName;
      RAISE NOTICE '';
      SELECT AVG(s_acctbal)
        INTO curNationAvgAccBal
      FROM supplier
      WHERE s_nationkey = suppCursor.s_nationkey;
      RAISE NOTICE '%  %  %  %',
                   RPAD('Supplier Name',20),
                   RPAD('Phone',15),
                   LPAD('Account Balance',20),
                   RPAD('Comment',60);
      RAISE NOTICE '';
    END IF;
    IF suppCursor.s_acctbal > curNationAvgAccBal THEN
      aComment := 'Above nation avg of '
                  || TO_CHAR(curNationAvgAccBal,'FM$9,999,999.00');
    ELSE
      aComment := 'Below nation avg of '
                  || TO_CHAR(curNationAvgAccBal,'FM$9,999,999.00');
    END IF;
    curSuppAcctBal := suppCursor.s_acctbal;
    RAISE NOTICE '%  %  %  %',
                 RPAD(suppCursor.s_name,20),
                 RPAD(suppCursor.s_phone,15),
                 LPAD(TO_CHAR(curSuppAcctBal,'FM$9,999,999.00'),20),
                 RPAD(aComment,60);
  END LOOP;
 END;
 $SUPPLIERACCBAL$;-- Example call:
 CALL SUPPLIERACCBAL(1);