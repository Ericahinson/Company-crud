from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblstores_payment
stores_paymenttbl_create = """CREATE TABLE `company_db`.`tblstores_payment` (
`bank_account_id` INT,
`stores_id` INT,
`payment_amount` VARCHAR(45) NULL,
FOREIGN KEY (`stores_id`)) REFERENCES tblsalesperson (`salesperson_id`)"""


c.execute(stores_paymenttbl_create)

c = db.cursor()

# fetch tblproduct details in the database
c.execute("desc tblstores_payment")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()

