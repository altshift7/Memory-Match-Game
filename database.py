import sqlite3

def init_db():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    level INTEGER,
                    time_taken INTEGER,
                    clicks INTEGER
                )''')
    conn.commit()
    conn.close()

def save_score(username, level, time_taken, clicks):
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (username, level, time_taken, clicks) VALUES (?, ?, ?, ?)",
              (username, level, time_taken, clicks))
    conn.commit()
    conn.close()

def get_top_scores(level):
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("SELECT username, time_taken, clicks FROM leaderboard WHERE level=? ORDER BY time_taken ASC LIMIT 5", (level,))
    rows = c.fetchall()
    conn.close()
    return rows
