import sqlite3 
from chatbox_server import user_info

db_name = "quiz.sqlite"
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()

#user info table(I hope it'll work)
do("CREATE TABLE user_info(username PRIMARY KEY, email VARCHAR, password VARCHAR)")

def fill_info():
    user_info()
    do("INSERT INTO user_info(username, email, password) VALUES (username1, email1, password1)")
