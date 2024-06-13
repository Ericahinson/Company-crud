from main import connect_to_database

# Establish database connection
db = connect_to_database()

# cursor object c
c = db.cursor()

# create statement for tblsales
salestbl_create = """CREATE TABLE `company_db`.`tblsales` (
`salesid` INT NOT NULL AUTO_INCREMENT,
`customer_id` INT,
`salesperson_id` INT,
`salesdate` DATE NULL,
PRIMARY KEY (`salesid`))
FOREIGN KEY (`customer_id`) REFERENCES tblcustomer (`customer_id`),
FOREIGN KEY (`salesperson_id`) REFERENCES tblsalesperson (`salesperson_id`)"""


c.execute(salestbl_create)

c = db.cursor()

# fetch tblsales details in the database
c.execute("desc tblsales")

# print the table details
for i in c:
	print(i)


# finally closing the database connection
db.close()
