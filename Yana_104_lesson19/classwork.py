# Ȁапишите декоратор, который будет считать, сколько раз была вызвана
# декорируемая функция

count_ = 0


def count_funk(funk):
    def f():
        global count_
        funk()
        count_ += 1
        return funk()

    return f


@count_funk
def re():
    return 2 + 8


@count_funk
def re():
    return 2 + 8


print(count_)
