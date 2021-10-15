import sqlite3

conn = sqlite3.connect('newdb.sqlite')
cur = conn.cursor()

table_schema = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
); 
"""

cur.execute(table_schema)

result = cur.fetchall()
print(result)

cur.close()

conn.close()
