# Data Access Object

import mysql.connector

cnx = mysql.connector.connect(user='root', password='Alpine@187',
                              host='127.0.0.1',
                              database='grocery_store')


cursor = cnx.cursor()

query = "SELECT * FROM grocery_store.orders_table"

cursor.execute(query)

for (name) in cursor:
    print(name) 

cnx.close()