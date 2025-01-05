--Set Up the SQL Database to store visitors details

--Create a Database

CREATE DATABASE website_visitors;

--Create a Table for Storing Visitor Data

USE website_visitors;

CREATE TABLE visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT NOT NULL,
    visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
