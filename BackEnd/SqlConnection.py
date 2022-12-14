import csv
import mysql.connector
import pandas as pd
import sys


""""
    This class is used to connect to the database, read the final csv file from the Attendance 
     and insert the data into the database.
"""


class SqlConnetion:

    def ConnectDB(self):
        mydb = mysql.connector.connect(
            user='root',
            password='root',
            host='db',
            port='3306',
            database='Attendance',
        )
        return mydb

    def SqlDataBase(self):
        # save attendance path dir
        csvFile = 'attendance.csv'
        mydb = mysql.connector.connect(
            user='root',
            password='root',
            host='db',
            port='3306',
            database='Attendance',
        )
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Attendance")
        cursor.execute("USE Attendance")
        cursor.execute("DROP TABLE IF EXISTS Attendance")
        cursor.execute(
            "CREATE TABLE Attendance (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Average VARCHAR(255))")
        # insert data just name and average into table
        with open(csvFile, 'r') as f:
            reader = csv.reader(f)
            headerList = next(reader)
            for row in reader:
                cursor.execute(
                    "INSERT INTO Attendance (Name, Average) VALUES (%s, %s)", (row[1], row[4]))
        mydb.commit()
        cursor.close()
        return mydb
