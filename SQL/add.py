import sqlite3 as sl

con = sl.connect('inter.db')
'''
INSERT INTO table_name (id, name, make, model, year) 
VALUES (1, 'Marly', 'Ford', 'Explorer', '2000');

sql = 'INSERT INTO inter (id, name, make, model, year) '''

sql = 'INSERT INTO USER (id, name, age, email, mobile) values(?, ?, ?, ?, ?)'
data = [
        (4, 'Alice', 25, '@yandex.ru', '+79992341234'),
        (5, 'Bob', 26, '@mail.ru', '+79992344321'),
        (6, 'Chris', 27, '@wer.ru', '+79998882233')
]

with con:
    con.executemany(sql, data)