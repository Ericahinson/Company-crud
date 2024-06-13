from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblbank_account
bank_accounttbl_create = """CREATE TABLE `company_db`.`tblbank_account` (
`bank_account_id` INT NOT NULL AUTO_INCREMENT,
`bank_account_name` VARCHAR(45) NULL,
`bank_name` VARCHAR(45) NULL,
`bank_branch` VARCHAR(20) NULL,
PRIMARY KEY (`bank_account_id`))"""

c.execute(bank_accounttbl_create)

c = db.cursor()

# fetch tblbank_account details in the database
c.execute("desc tblbank_account")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
