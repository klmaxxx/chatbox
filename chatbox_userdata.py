import sqlite3 

db_name = "quiz.sqlite"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

#user info table(I hope it'll work)
cursor.execute("CREATE TABLE IF NOT EXISTS user_info(username PRIMARY KEY, email VARCHAR, password VARCHAR)")

def fill_info():
    cursor.execute("INSERT INTO user_info(username, email, password) VALUES (username1, email1, password1)")
    conn.commit()
