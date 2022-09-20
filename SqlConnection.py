import csv
import mysql.connector
import pandas as pd
import sys


#
#
class SqlConnetion:

    def ConnectDB(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="malchital1",
        )
        return mydb


    def SqlDataBase(self):
        # save attendance path dir
        csvFile = 'attendance.csv'
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="malchital1",
        )
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Attendence")
        cursor.execute("USE Attendence")
        cursor.execute("DROP TABLE IF EXISTS Attendence")
        cursor.execute(
            "CREATE TABLE Attendence (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Average VARCHAR(255))")
        # insert data just name and average into table
        with open(csvFile, 'r') as f:
            reader = csv.reader(f)
            headerList = next(reader)
            for row in reader:
                cursor.execute("INSERT INTO Attendence (Name, Average) VALUES (%s, %s)", (row[1], row[4]))
        mydb.commit()
        cursor.close()
        return mydb

# SqlDataBase(sys.argv[1]) if len(sys.argv) == 2 else print("Invalid argument")
