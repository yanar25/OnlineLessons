# Ȁапишите декоратор debug, который при каждом вызове
# декорируемой функции выводит её имя (вместе со всеми
# передаваемыми аргументами), а затем — какое значение
# она возвращает. Ȃосле этого выводится результат её
# выполнения

def debug(func):
    def df(*args, **kwargs):
        funcname = func.__name__, args, kwargs
        print(funcname)
        func()

    return df()


@debug
def cat():
    print('catt')
