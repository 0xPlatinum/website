import sqlite3

connection = sqlite3.connect('logs.db')

cur = connection.cursor()


connection.commit()
connection.close()