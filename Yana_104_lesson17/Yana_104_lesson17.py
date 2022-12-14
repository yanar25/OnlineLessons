# Два метода в классе, один принимает в себя либо
# строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв
# меньше или равно длине слова, выводить все
# гласные, иначе согласные;
# если число то, произведение суммы чётных цифр
# на длину числа.

class clss:
    def int_str(self, objct):  # обьявление метода
        if type(objct) == str:  # если тип обьекта строка
            vowel = 0
            consonant = 0
            letters = ''
            for i in objct:  # итерация по обьекту
                if i in 'aeyuio':  # проверка на гласность
                    vowel += 1  # в случае тру добавляет единицу в счесчик гласных
                else:  # иначе добавляет в счетчик согласных. элементы которые не являются
                    # буквами так же считаются за согласные
                    consonant += 1

            for i in objct:  # повторная итерация по обьекту
                if vowel * consonant <= len(objct):  # если гласные умножить на согласные меньше длины обьекта
                    if i in 'aeyuio':
                        letters += i
                else:
                    if i not in 'aeyuio':
                        letters += i
            return letters  # возвращается строка только с гласными или согласными буквами

        elif type(objct) == int or type(objct) == float:  # если обьект - инт или флоат типа
            even = 0  # счетчик четных чисел
            for i in str(objct):  # итерация по обьекту приведенному к строке
                if int(i) % 2 == 0:  # проверка инт цифры на четность
                    even += int(i)  # добавление в счетчик
            return even * len(str(objct))  # возвращает длину обьекта умноженную на значение счетчика


obj = clss()
print(obj.int_str(123))
print(obj.int_str('cat'))
