# Задача:
# 1. Дан список [ [1,2,3], [4, 5, 6], [7, 8, 9] ]
# 2. Напишите функцию, которая возвращает новый список, состоящий из
# значений кратных 3.
# 3. Напишите декоратор, который будет возвращать количество значений,
# не кратных 3 из вашей функции.
import functools


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

    return new_list


lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lst(lists))


def not3(func):
    @functools.wraps(func)
    def n3(*args, **kwargs):
        aa = [repr(a) for a in *args]
