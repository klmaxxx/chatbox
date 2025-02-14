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


# user info table(I hope it'll work)
execute(
    "CREATE TABLE IF NOT EXISTS user_info(id INTEGER PRIMARY KEY, username VARCHAR, email VARCHAR, password VARCHAR)"
)


def fill_info(username: str, email: str, password: str):
    execute(
        "INSERT INTO user_info(username, email, password) VALUES (?, ?, ?)",
        [username, email, password],
    )
    print(*execute("SELECT * FROM user_info"), sep="\n", flush=True)


def valid_user(username, password):
    return bool(
        execute(
            "SELECT ROWID, * FROM user_info WHERE username == ? AND password == ? LIMIT 1",
            [username, password],
        )
    )


def user_exists(name, email):
    return bool(
        execute("SELECT * FROM user_info WHERE username == ? OR email == ? LIMIT 1", [name, email])
    )


def get_all_users():
    return execute("SELECT ROWID, * FROM user_info")


def get_user(name):
    return execute("SELECT ROWID, * FROM user_info WHERE username == ? LIMIT 1", [name])[0]
