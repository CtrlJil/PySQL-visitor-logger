#Connect to the Database

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website_visitors"
)
cursor = db.cursor()

#Retrieve All Visitor Records

cursor.execute("SELECT * FROM visitors ORDER BY visit_time DESC")
for row in cursor.fetchall():
    print(row)

#Count Unique Visitors

cursor.execute("SELECT COUNT(DISTINCT ip_address) FROM visitors")
print("Unique Visitors:", cursor.fetchone()[0])
