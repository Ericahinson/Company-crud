from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblpurchase
purchasetbl_create = """CREATE TABLE `company_db`.`tblpurchase` (
`purchase_id` INT NOT NULL AUTO_INCREMENT,
`pdid` INT NOT NULL AUTO_INCREMENT,
`suppliers_id` INT NOT NULL AUTO_INCREMENT,
`stores_id` INT NOT NULL AUTO_INCREMENT,
`purchase_balance` VARCHAR(45) NULL,
`invoice` VARCHAR(45) NULL,
PRIMARY KEY (`purchase_id`))
FOREIGN KEY (`pdid`)) REFERENCES tblproduct (`pdid`),
FOREIGN KEY (`suppliers_id`)) REFERENCES tblsuppliers (`suppliers_id`),
FOREIGN KEY (`stores_id`)) REFERENCES tblstores (`stores_id`)"""

c.execute(purchasetbl_create)

c = db.cursor()

# fetch tblpurchase details in the database
c.execute("desc tblpurchase")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
