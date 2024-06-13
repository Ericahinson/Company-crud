from main import connect_to_database

# Establish database connection
db = connect_to_database()

# Create a cursor object
cursor = db.cursor()
 
# Prepare the SQL query
sql = "INSERT INTO tblcustomers (customer_id, customer_name, customer_number) VALUES (%s, %s, %s)"
values = ("102", "John Smith", "0594674893")
 
# Execute the query
cursor.execute(sql, values)
 
# Commit the changes
db.commit()
 
# Print the number of rows affected
print(cursor.rowcount, "record inserted.")
