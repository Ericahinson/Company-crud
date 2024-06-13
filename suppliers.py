from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblsuppliers
supplierstbl_create = """CREATE TABLE `company_db`.`tblsuppliers` (
`suppliers_id` INT NOT NULL AUTO_INCREMENT,
`supplier_name` VARCHAR(45) NULL,
`supplier_email` VARCHAR(45) NULL,
PRIMARY KEY (`suppliers_id`))"""

c.execute(supplierstbl_create)

c = db.cursor()

# fetch tblsuppliers details in the database
c.execute("desc tblsuppliers")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
