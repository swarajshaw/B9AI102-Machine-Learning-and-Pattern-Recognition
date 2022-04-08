import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="swaraj",
    database="amazon-db"
)
# Creating Cursor object

mycursor = mydb.cursor()

# Creating the Table in MySQL Database

mycursor.execute("create table Books (TS TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),Title Varchar(255),Price float(23,2),Rating float(23,1))")

# Making the SQL Insert Query

sql = "INSERT INTO Books (Title, Price, Rating) VALUES (%s, %s, %s)"

# Executing Insert Query and using List of Tuple as Values
mycursor.executemany(sql, Data)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mydb.close()
