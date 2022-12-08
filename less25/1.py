
import sqlite3  # импортируем соответствующий модуль
conn = sqlite3.connect('name.db')

cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
        tab_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col_1 TEXT,
        col_2 TEXT
    )
    ''')


cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES('hello','world')
''')
# ОБЯЗАТЕЛЬНО СОХРАНЯЕМ ИЗМЕНЕНИЯ
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
    tab_2(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        col_1 TEXT, 
        col_2 TEXT
    )
""")

var1 = "red"
var2 = "black"

command = """ 
    INSERT INTO tab_2(col_1, col_2) 
    VALUES(?,?)
"""

cursor.execute(""" 
    INSERT INTO tab_2(col_1, col_2) 
    VALUES(?,?)
""", (var1, var2))

datalist = [('yellow', 'white') for x in range(10)]

for tuple in datalist:
    cursor.execute(command, tuple)


conn.commit()
#
# cursor.execute('''SELECT * FROM tab_2''')
# print(cursor.fetchall())


