# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в
# соответствующую таблицу, затем посчитать длину слова и
# записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное
# записать его в таблицу чисел, если нечётное, то записать во
# вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить
# 1 запись в первой таблице. Если меньше, то обновить 1
# запись в первой таблице на «hello»

import sqlite3

listt = ['gg', 2, 87687678, 'fgvhfgh', 'fghfghgh']
conn = sqlite3.connect('namme.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS xtx(id INTEGER PRIMARY KEY AUTOINCREMENT, strr TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS tni(id INTEGER PRIMARY KEY AUTOINCREMENT, intt INTEGER)")
for i in listt:
    if type(i) == str:
        cursor.execute("""INSERT INTO xtx(strr) VALUES (?)""", (i,))
        cursor.execute("""INSERT INTO tni(intt) VALUES (?)""", (len(i),))
    elif type(i) == int:
        if i % 2 == 0:
            # print(i)
            cursor.execute("""INSERT INTO tni(intt) VALUES (?)""", (i,))
        else:
            # print('gh')
            cursor.execute("""INSERT INTO xtx(strr) VALUES ('нечетное')""")

conn.commit()
cursor.execute("""SELECT * FROM tni""")
k2 = cursor.fetchall()
if len(k2) > 5:
    cursor.execute("""SELECT * FROM xtx""")
    k1 = cursor.fetchall()
    del k1[0]
else:
    cursor.execute("UPDATE xtx SET strr='hello' WHERE id=1")
cursor.execute("""SELECT * FROM xtx""")
k1 = cursor.fetchall()
print(k1)
cursor.execute("""SELECT * FROM tni""")
k2 = cursor.fetchall()
print(k2)
