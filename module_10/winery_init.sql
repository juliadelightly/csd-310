-- drop test user if exists 
DROP USER IF EXISTS 'winery_employee'@'localhost';


-- create pysports_user and grant them all privileges to the winery database 
CREATE USER 'winery_employee'@'localhost' IDENTIFIED WITH mysql_native_password BY 'JKD@sql22!';

-- grant all privileges to the pysports database to user winery_employee on localhost 
GRANT ALL PRIVILEGES ON winery.* TO'winery_employee'@'localhost';

ALTER TABLE delivery_metrics
DROP CONSTRAINT fk_suppliers;
ALTER TABLE distributor
DROP CONSTRAINT fk_wine;
ALTER TABLE time_sheet
DROP CONSTRAINT fk_employee;


-- drop tables if they are present
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS wine;
DROP TABLE IF EXISTS delivery_metrics;
DROP TABLE IF EXISTS distributor;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS time_sheet;






-- create the products table and set the attributes
CREATE TABLE winery.suppliers (
    supplier_id             INT        NOT NULL AUTO_INCREMENT,
    supplier_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY (supplier_id)
);

CREATE TABLE winery.delivery_metrics (
    delivery_id            INT        NOT NULL AUTO_INCREMENT,
    supplier_id             INT       NOT NULL,        
    expected_deliverytime   VARCHAR(75)  NOT NULL,        
    actual_deliverytime     VARCHAR(75)  NOT NULL,
    delivery_gap            VARCHAR(75)  NOT NULL,
    month           VARCHAR(75)       NOT NULL,
    PRIMARY KEY (delivery_id),
    CONSTRAINT fk_suppliers
    FOREIGN KEY (supplier_id)
      REFERENCES suppliers(supplier_id)
);

CREATE TABLE winery.wine (
   name          VARCHAR(75)        NOT NULL,   
   upc           INT                NOT NULL,
   PRIMARY KEY (upc)
   
);

CREATE TABLE winery.distributor (
   distributor_id     INT           NOT NULL   AUTO_INCREMENT,
   distributor_name  VARCHAR(75)    NOT NULL,
   pickup_time       VARCHAR(75)    NOT NULL,
   units              INT           NOT NULL,
   order_id           INT           NOT NULL,
   upc                INT           NOT NULL,
   PRIMARY KEY (distributor_id),
   CONSTRAINT fk_wine
   FOREIGN KEY (upc)
     REFERENCES wine(upc)

);


CREATE TABLE winery.employee (
    employee_id      INT                NOT NULL AUTO_INCREMENT,
    first_name       VARCHAR(75)        NOT NULL,
    last_name        VARCHAR(75)        NOT NULL,
    job_title        VARCHAR(75)        NOT NULL,
    PRIMARY KEY(employee_id)
);
CREATE TABLE winery.time_sheet (
    employee_id                INT     NOT NULL,
    time_worked                VARCHAR(75) NOT NULL,
    quarter                    INT     NOT NULL,
   CONSTRAINT fk_employee
   FOREIGN KEY (employee_id)
     REFERENCES employee(employee_id)

);