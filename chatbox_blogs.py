import sqlite3
from contextlib import closing
from typing import Any

DB_NAME = "blog.sqlite"


def execute(query: str, params: list[Any] | None = None):
    """Виконує один запит з необов'язковими параметрами."""

    with closing(sqlite3.connect(DB_NAME)) as conn:
        with conn:  # Автоматичне збереження (commit) змін
            with closing(conn.cursor()) as cursor:
                cursor.execute(query, params or [])
                return cursor.fetchall()  # Повертає всі результати для SELECT-запитів.


# user info table(I hope it'll work)
execute("CREATE TABLE IF NOT EXISTS blog(id INTEGER PRIMARY KEY, post VARCHAR)")


def fill_blogs(blog):
    execute("INSERT INTO blog(post) VALUES (?)", [blog])
