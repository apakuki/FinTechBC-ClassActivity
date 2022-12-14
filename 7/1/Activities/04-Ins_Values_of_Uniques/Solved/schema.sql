-- Drop "customer" table if exists
DROP TABLE IF EXISTS customer;

-- Create the table "customer"
CREATE TABLE customer (
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30),
  gender VARCHAR(30),
  age INT,
  address VARCHAR(50),
  city VARCHAR(50),
  province CHAR(2),
  postal_code CHAR(6)
);

-- Re-create the table "customer"
-- with an incremental primary key
CREATE TABLE customer (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30),
  gender VARCHAR(30),
  age INT,
  address VARCHAR(50),
  city VARCHAR(50),
  province CHAR(2),
  postal_code CHAR(6)
);
