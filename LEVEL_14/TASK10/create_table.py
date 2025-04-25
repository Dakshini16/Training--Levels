import sqlite3

conn = sqlite3.connect("match_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS match_commentary (
        year INTEGER,
        series_type TEXT,
        series_name TEXT,
        match_no TEXT,
        match_type TEXT,
        match_id INTEGER,
        ball_no TEXT,
        over_no TEXT,
        ball_commentary TEXT
    )
''')

conn.commit()
conn.close()
print("Table created successfully.")
