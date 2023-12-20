import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SchoolMySQL55!",
  database="uzņēmums"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Darbinieki (id INT AUTO_INCREMENT PRIMARY KEY, vārds VARCHAR(255), uzvārds VARCHAR(255), vecums CHAR(3), pilsēta VARCHAR(255), adrese VARCHAR(255), telefona_numurs CHAR(8))")