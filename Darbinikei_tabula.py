import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SchoolMySQL55!",
  database="world"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Darbinieki (name VARCHAR(255), address VARCHAR(255))")