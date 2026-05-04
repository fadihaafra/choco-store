import sqlite3

conn = sqlite3.connect('chocolates.db')
c = conn.cursor()

c.execute("SELECT * FROM orders")
print(c.fetchall())

conn.close()