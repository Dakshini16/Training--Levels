import sqlite3

conn = sqlite3.connect("match_data.db")
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO match_commentary (
        year, series_type, series_name, match_no, match_type,
        match_id, ball_no, over_no, ball_commentary
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    2021, 'League', 'Indian Premier League 2021', '1st Match', 'T20 IPL',
    35612, '1.1', '1', 'Rohit Sharma flicks to square leg for a single'
))

conn.commit()
conn.close()
print("Sample data inserted.")
