from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblstores
storestbl_create = """CREATE TABLE `company_db`.`tblstores` (
`stores_id` INT NOT NULL AUTO_INCREMENT,
`stores_name` VARCHAR(45) NULL,
`stores_number` VARCHAR(10) NULL,
PRIMARY KEY (`stores_id`))"""

c.execute(storestbl_create)

c = db.cursor()

# fetch tblproduct details in the database
c.execute("desc tblstores")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
