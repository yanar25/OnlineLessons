# Задача:
# 1. Дан список [ [1,2,3], [4, 5, 6], [7, 8, 9] ]
# 2. Напишите функцию, которая возвращает новый список, состоящий из
# значений кратных 3.
# 3. Напишите декоратор, который будет возвращать количество значений,
# не кратных 3 из вашей функции.
import functools


# задача не решена

def lst(listt):
    new_list = []

    def true_lst(x=listt):
        nonlocal new_list
        for i in x:
            if type(i) == list:
                true_lst(i)
            else:
                if i % 3 == 0:
                    new_list.append(i)

    true_lst()
    print(new_list)

    return new_list


def not3(listt):
    listnot3 = []

    def n3(*arg):
        nonlocal listnot3
        for i in arg:
            if type(i) == list:
                n3(i)
            else:
                if i % 3 != 0:
                    listnot3.append(i)

    print(n3(listt))
    n3(listt)

    return listnot3


lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

not3(lst(lists))
