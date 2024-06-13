from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblcustomer
customertbl_create = """CREATE TABLE `company_db`.`tblcustomer` (
`customer_id` INT NOT NULL AUTO_INCREMENT,
`customer_name` VARCHAR(45) NULL,
`customer_number` VARCHAR(10) NULL,
PRIMARY KEY (`customer_id`))"""

c.execute(customertbl_create)

c = db.cursor()

# fetch tblcustomer details in the database
c.execute("desc tblcustomer")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
