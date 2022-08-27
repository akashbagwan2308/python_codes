# insert data into table using python
import sqlite3

con = sqlite3.connect('OurDB.db')
cur = con.cursor()
cur.execute('INSERT INTO Product(p_id,p_name,price,quantity) Values(01,"AutoCAD",200,20)')
cur.execute('INSERT INTO Product(p_id,p_name,price,quantity) Values(02,"Monitor",1000,5)')
cur.execute('INSERT INTO Product(p_id,p_name,price,quantity) Values(03,"Printer",500,15)')
cur.execute('INSERT INTO Product(p_id,p_name,price,quantity) Values(04,"Keyboard",100,25)')

print("Data Inserted")
con.commit()
con.close() 