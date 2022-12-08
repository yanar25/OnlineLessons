# Задание №1
# Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно
# – целое число. Число запрашивается с клавиатуры, а слова
# задаются статически.
# * Выведите каждую запись в отдельную строку
import random
import sqlite3

conn = sqlite3.connect('name2.bd')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tabble(id INTEGER PRIMARY KEY AUTOINCREMENT, p1 TEXT, p2 TEXT, p3 INTEGER)")
conn.commit()
p11 = input('p1: ')
p22 = input('p2: ')
p33 = random.randint(1, 13436)
cursor.execute("INSERT INTO tabble(p1, p2, p3) VALUES (?, ?, ?)", (p11, p22, p33))
conn.commit()
cursor.execute('SELECT p1 FROM tabble')
c = cursor.fetchall()
print(c)