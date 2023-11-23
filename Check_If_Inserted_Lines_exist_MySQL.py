import mysql.connector

mydb = mysql.connector.connect(
    host = "Localhost",
    user = "root",
    password = "SchoolMySQL55!", 
    database = "world"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM newtabletest")

myresult = mycursor.fetchall()

for x in myresult:

    print(x)