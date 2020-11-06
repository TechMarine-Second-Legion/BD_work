import sqlite3 as sl

con = sl.connect('inter.db')
cur = sl.Cursor
#DELETE FROM table_name 
#WHERE name='Ford';

sql = "DELETE FROM USER WHERE name = 'Alice'"

#sql = 'INSERT INTO USER (id, name, age, email, mobile) values(?, ?, ?, ?, ?)'

#cur.execute("DELETE FROM USER WHERE name='Alice';")
#conn.commit()

#with con:
#    con.executemany(sql, data)