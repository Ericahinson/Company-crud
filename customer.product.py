from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblcustomer_product
customer_producttbl_create = """CREATE TABLE `company_db`.`tblcustomer_product` (
`customer_id` INT NOT NULL AUTO_INCREMENT,
`pdid` INT NOT NULL AUTO_INCREMENT,
`product_price` VARCHAR(45) NULL,
`product_value` VARCHAR(45) NULL,
`product_quantity` VARCHAR(45) NULL,
FOREIGN KEY (`pdid`)) REFERENCES tblproduct (`pdid`),
FOREIGN KEY (`customer_id`)) REFERENCES tblcustomer (`customer_id`)"""

c.execute(customer_producttbl_create)

c = db.cursor()

# fetch tblcustomer_product details in the database
c.execute("desc tblcustomer_product")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
