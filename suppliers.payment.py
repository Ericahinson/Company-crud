from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblproduct
suppliers_paymenttbl_create = """CREATE TABLE `company_db`.`tblsuppliers_payment` (
`bank_account_id` INT NOT NULL AUTO_INCREMENT,
`bank_account_name` VARCHAR(45) NULL,
`amount` INT NULL,
PRIMARY KEY (`bank_account_id`))"""

c.execute(suppliers_paymenttbl_create)

c = db.cursor()

# fetch tblsuppliers_payment details in the database
c.execute("desc tblsuppliers_payment")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
