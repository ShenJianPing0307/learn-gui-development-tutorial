import sqlite3

conn = sqlite3.connect('mrsoft.db')

cursor = conn.cursor()

cursor.execute('insert into user(id, name) values ("1", "MRSOFT")')

cursor.close()
conn.commit()