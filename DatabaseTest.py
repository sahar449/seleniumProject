import mysql.connector

doConnector = mysql.connector.connect(
    host="localhost",
    user="Sahar",
    password="302885041s",
    database="sahar"
)

cursor = doConnector.cursor()

# print all tables in the database
cursor.execute("SHOW TABLES")
result = cursor.fetchall()
for x in result:
    print(x)


cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
print(result)



