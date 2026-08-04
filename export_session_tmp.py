import sqlite3, json, sys, os, datetime

db_path = r'C:\Users\x2\.local\share\opencode\opencode.db'
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print("TABLES:", tables)