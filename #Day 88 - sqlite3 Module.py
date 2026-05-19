#Day 88 - sqlite3 Module 
import sqlite3

conn = sqlite3.connect('day88.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
conn.commit()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()
print("Users:", rows)

conn.close()