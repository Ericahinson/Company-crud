from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblproduct_sales
product_salestbl_create = """CREATE TABLE `company_db`.`tblproduct_sales` (
`salesid` INT NOT NULL AUTO_INCREMENT,
`salesperson_id` INT NOT NULL AUTO_INCREMENT,
`pdid` INT NOT NULL AUTO_INCREMENT,
`customer_id` INT NOT NULL AUTO_INCREMENT,
`bank_account_id` INT NOT NULL AUTO_INCREMENT,
FOREIGN KEY (`pdid`)) REFERENCES tblproduct (`pdid`),
FOREIGN KEY (`sales_id`)) REFERENCES tblsales (`sales_id`),
FOREIGN KEY (`customer_id`)) REFERENCES tblcustomer (`customer_id`),
FOREIGN KEY (`bank_account_id`)) REFERENCES tblbank_account (`bank_account_id`),
FOREIGN KEY (`salesperson_id`)) REFERENCES tblsalesperson (`salesperson_id`)"""

c.execute(product_salestbl_create)

c = db.cursor()

# fetch tblproduct_sales details in the database
c.execute("desc tblproduct_sales")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()


