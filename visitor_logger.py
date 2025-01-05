#install flask to handle http requests
#install mysql-connector-python to interact with databases 
pip install flask mysql-connector-python

#Create a Python Flask Server
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the SQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website_visitors"
)
cursor = db.cursor()

@app.route('/track', methods=['GET'])
def track_visitor():
    # Get visitor details
    ip_address = request.remote_addr  # Visitor's IP address
    user_agent = request.headers.get('User-Agent')  # Browser details

    # Insert into MySQL
    cursor.execute("INSERT INTO visitors (ip_address, user_agent) VALUES (%s, %s)", (ip_address, user_agent))
    db.commit()

    return {"status": "Visitor Tracked", "ip": ip_address, "user_agent": user_agent}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
