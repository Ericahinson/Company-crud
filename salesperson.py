from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblsalesperson
salespersontbl_create = """CREATE TABLE `company_db`.`tblsalesperson` (
`salesperson_id` INT NOT NULL AUTO_INCREMENT,
`salesperson_name` VARCHAR(45) NULL,
`salesperson_number` VARCHAR(10) NULL,
PRIMARY KEY (`salesperson_id`))"""

c.execute(salespersontbl_create)

c = db.cursor()

# fetch tblsalesperson details in the database
c.execute("desc tblsalesperson")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
