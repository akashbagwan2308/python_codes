#connect to database to python
# import sqlite3
# con = sqlite3.connect('OurDB.db')
# print('You can see Database opened!')
# creating table in database using python
import sqlite3
con = sqlite3.connect('OurDB.db')
cur = con.cursor()
cur.execute('CREATE TABLE Product (p_id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT NOT NULL, price REAL,'
            'quantity INTEGER )')
print('Table created inside db')
con.close() 