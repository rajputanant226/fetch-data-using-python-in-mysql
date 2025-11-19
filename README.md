# Python–MySQL Connectivity README

This README explains how to connect Python with MySQL, create a cursor, fetch records, loop through rows, handle errors, and follow best practices.

## Prerequisites

Python installed

MySQL Server installed

MySQL Workbench or command-line access

mysql-connector-python package

Install MySQL connector:

pip install mysql-connector-python

1. Python–MySQL Connection Setup
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="testdb"
    )
    print("Connection Successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

2. How to Create a Cursor
cursor = connection.cursor()

3. Real Example – Sample Table

SQL to create a sample students table:

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    course VARCHAR(100)
);


Insert sample rows:

INSERT INTO students (name, course)
VALUES
('Anant', 'Python'),
('Riya', 'MySQL'),
('Saurabh', 'Data Science');

4. How to Fetch All Records
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

5. How to Loop Through Rows
for row in records:
    print(row)


Example output:

(1, 'Anant', 'Python')
(2, 'Riya', 'MySQL')
(3, 'Saurabh', 'Data Science')


6. Error Handling (Best Practice)

Use try–except to catch MySQL errors

Use finally block to close connection

Always check connection.is_connected() before closing

8. Best Practices Summary

Always close cursor and connection

Use readable variable names

Use try–except–finally for safety

Avoid hardcoding passwords in production

Validate database connection before executing queries
