from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblproduct
producttbl_create = """CREATE TABLE `company_db`.`tblproduct` (
`pdid` INT NOT NULL AUTO_INCREMENT,
`pdname` VARCHAR(45) NULL,
`description` VARCHAR(45) NULL,
`quantity` INT NULL,
`reorder` INT NULL,
`stock` INT NULL,
PRIMARY KEY (`pdid`))"""

c.execute(producttbl_create)

c = db.cursor()

# fetch tblproduct details in the database
c.execute("desc tblproduct")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
