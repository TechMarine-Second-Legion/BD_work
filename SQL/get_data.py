import sqlite3 as sl

con = sl.connect('inter.db')

with con:
    data = con.execute("SELECT * FROM USER WHERE age >= 12")
    for row in data:
        print(row)