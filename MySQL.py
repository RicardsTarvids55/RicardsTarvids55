import mysql.connector

mydb = mysql.connector.connect(
    host = "Localhost",
    User = "root",
    password = "SchoolMySQL55!" 
)

print (mydb)