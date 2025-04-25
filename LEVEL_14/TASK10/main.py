from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

class MatchCommentary(BaseModel):
    year: int
    series_type: str
    series_name: str
    match_no: str
    match_type: str
    match_id: int
    ball_no: str
    over_no: str
    ball_commentary: str

@app.get("/get/{match_id}", response_model=List[MatchCommentary])
def get_commentary(match_id: int):
    conn = sqlite3.connect("match_data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT year, series_type, series_name, match_no, match_type, match_id,
               ball_no, over_no, ball_commentary
        FROM match_commentary
        WHERE match_id = ?
    """, (match_id,))
    
    rows = cursor.fetchall()
    conn.close()
    
    # Convert each row to a dict matching the Pydantic model
    result = [
        {
            "year": row[0],
            "series_type": row[1],
            "series_name": row[2],
            "match_no": row[3],
            "match_type": row[4],
            "match_id": row[5],
            "ball_no": row[6],
            "over_no": row[7],
            "ball_commentary": row[8]
        }
        for row in rows
    ]
    
    return result
