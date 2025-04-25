import sqlite3

conn = sqlite3.connect("match_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM match_commentary")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
