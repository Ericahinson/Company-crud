from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblproduct_price
product_pricetbl_create = """CREATE TABLE `company_db`.`tblproduct_price` (
`product_id` INT NOT NULL AUTO_INCREMENT,
`product_price` VARCHAR(45) NULL,
FOREIGN KEY (`pdid`)) REFERENCES tblproduct (`pdid`)"""

c.execute(product_pricetbl_create)

c = db.cursor()

# fetch tblproduct_price details in the database
c.execute("desc tblproduct_price")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
