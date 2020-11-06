import sqlite3 as sl

con = sl.connect('testus.db')
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT,
            mobile TEXT
        );
    """)

sql = 'INSERT INTO USER (id, name, age, email, mobile) values(?, ?, ?, ?, ?)'
data = [
        (1, 'Alice', 21, '@yandex.ru', '+79992341234'),
        (2, 'Bob', 22, '@mail.ru', '+79992344321'),
        (3, 'Chris', 23, '@wer.ru', '+79998882233')
]

with con:
    con.executemany(sql, data)