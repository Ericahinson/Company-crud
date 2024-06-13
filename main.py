import mysql.connector

# Function to establish database connection
def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="company_db"
    )
    return db
