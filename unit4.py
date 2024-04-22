#creating the database
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='')
# mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

#Showing the list of database
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='')
# mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
# 	print(i)

#Creating the 'stud_data' Table
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE stud_data(roll int, name varchar(25))')

#Inserting the Records in the Table
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# insert_query = 'INSERT INTO stud_data (roll, name) VALUES(%s, %s)'
# records_insert = [(1,'sunday'),(2,'monday'), (3,'saturday')]
# mycursor = mydb.cursor()
# mycursor.executemany(insert_query,records_insert)
# mydb.commit()
# print('Record inserted successfully')
# mydb.close()

#Inserting the Records in the Table using try-except
# import mysql.connector
# try:
# 	mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# 	insert_query = 'INSERT INTO stud_data (roll, name) VALUES(%s, %s)'
# 	records_insert = [(1,'wednesday'),(2,'thursday'), (3,'friday')]
# 	mycursor = mydb.cursor()
# 	mycursor.executemany(insert_query,records_insert)
# 	mydb.commit()
# 	print('Record inserted successfully')
# except mysql.connector.Error as error:
# 	print('Failed to insert a record')
# mydb.close()

#Display the records inserted in the table
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# mycursor = mydb.cursor()
# mycursor.execute('SELECT * FROM stud_data')
# result = mycursor.fetchall()
# for i in result:
# 	print(i)
# print(result)

#Updating the Record
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# mycursor = mydb.cursor()
# Update_query = "UPDATE stud_data SET roll=5 WHERE name='monday'"
# mycursor.execute(Update_query)
# mydb.commit()

# Deleting the Record
# import mysql.connector
# mydb = mysql.connector.connect(host='localhost', user='root', password='', database='mypy')
# mycursor = mydb.cursor()
# delete_query = "DELETE FROM stud_data WHERE roll=5"
# mycursor.execute(delete_query)
# mydb.commit()


