#Day 88 - SQLite Helper
import sqlite3

conn = sqlite3.connect('day88.db')
cur = conn.cursor()

cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
print("Tables:", cur.fetchall())

cur.execute('SELECT name, age FROM users WHERE age > ?', (26,))
print("Filtered:", cur.fetchall())

conn.close()