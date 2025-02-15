import sqlite3
from contextlib import closing
from typing import Any

DB_NAME = "user_data.sqlite"


def execute(query: str, params: list[Any] | None = None):
    """Виконує один запит з необов'язковими параметрами."""

    with closing(sqlite3.connect(DB_NAME)) as conn:
        with conn:  # Автоматичне збереження (commit) змін
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params or [])
                return cursor.fetchall()  # Повертає всі результати для SELECT-запитів.


def create_tables():
    execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username VARCHAR NOT NULL, email VARCHAR NOT NULL, password VARCHAR NOT NULL)"
    )
    execute(
        "CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, text VARCHAR NOT NULL, FOREIGN KEY (author_id) REFERENCES users (id))"
    )


def fill_info(username: str, email: str, password: str):
    execute(
        "INSERT INTO users(username, email, password) VALUES (?, ?, ?)",
        [username, email, password],
    )
    print(*execute("SELECT * FROM users"), sep="\n", flush=True)


def valid_user(username, password):
    return bool(
        execute(
            "SELECT ROWID, * FROM users WHERE username == ? AND password == ? LIMIT 1",
            [username, password],
        )
    )


def user_exists(name, email):
    return bool(
        execute("SELECT * FROM users WHERE username == ? OR email == ? LIMIT 1", [name, email])
    )


def get_all_users():
    return execute("SELECT ROWID, * FROM users")


def get_user(name):
    return execute("SELECT * FROM users WHERE username == ? LIMIT 1", [name])[0]


def fill_posts(user_id, text):
    execute("INSERT INTO posts (author_id, text) VALUES (?, ?)", [user_id, text])


def get_posts(limit=20, offset=0):
    return execute(
        """
        SELECT username, text 
        FROM posts 
        JOIN users ON users.id = posts.author_id 
        ORDER BY posts.created DESC 
        LIMIT ? OFFSET ?
        """,
        [limit, (offset - 1) * limit],
    )


if __name__ == "__main__":
    # create_tables()
    pass
