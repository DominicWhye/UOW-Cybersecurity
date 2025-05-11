-- Task 3: Trigger for CUSTOMER.c_comment-- 1) Trigger function
 CREATE OR REPLACE FUNCTION set_customer_comment()
  RETURNS TRIGGER
 LANGUAGE plpgsql AS
 $$
 BEGIN
    IF NEW.c_comment IS NULL THEN
        NEW.c_comment := 'New customer was created on '
                         || TO_CHAR(CURRENT_DATE,'YYYY-MM-DD');
    END IF;
    RETURN NEW;
 END;
 $$;-- 2) Attach trigger
 DROP TRIGGER IF EXISTS trg_set_customer_comment ON customer;
 CREATE TRIGGER trg_set_customer_comment
  BEFORE INSERT ON customer
  FOR EACH ROW
  EXECUTE PROCEDURE set_customer_comment();-- Example insert:
 INSERT INTO customer (
  c_custkey, c_name, c_address, c_nationkey,
  c_phone, c_acctbal, c_mktsegment, c_comment
 ) VALUES (
  999999, 'Test Cust', '123 Elm St', 1,
  '000-000-0000', 100.00, 'BUILDING', NULL
 );