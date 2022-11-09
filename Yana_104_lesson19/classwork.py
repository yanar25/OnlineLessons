# Ȁапишите декоратор, который будет считать, сколько раз была вызвана
# декорируемая функция

count_ = 0


def count_funk(funk):
    def f(*arg):
        print(arg)
        global count_
        fun = funk(arg)
        count_ += 1
        return fun

    return f


@count_funk
def re(a):
    print(a)
    return 2 + 8


print(count_funk(re(3)))
print(count_funk(re(3)))
print(count_)
