# Домашнее задание
# Класс Tomato:
# 1. Ȅоздайте класс Tomato
# 2. Ȅоздайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Ȅоздайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1)
# _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Ȅоздайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Ȅоздайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# 1. Ȅоздайте класс TomatoBush
# 2. ȁпределите метод __init__(), который будет принимать в качестве параметра количество томатов и на его
# основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри
# динамического свойства tomatoes.
# 3. Ȅоздайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап
# созревания
# 4. Ȅоздайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Ȅоздайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# 1. Ȅоздайте класс Gardener
# 2. Ȅоздайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name -
# передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является
# protected
# 3. Ȅоздайте метод work(), который заставляет садовника работать, что позволяет растению становиться
# более зрелым
# 4. Ȅоздайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# 5. Ȅоздайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
import random


# каюсь, это очень грязный и плохочитаемый код, но из за одной цепочки ошибок которые я исправляла несколько часов
# уже поросто нет сил его подчистить и доработать. в следующий раз постараюсь хоть как то исправиться

class Tomato:

    def __init__(self, st=1):
        # self.st = 1
        self._st = st  # ate = Tomato.states(self)[self.st]

    @staticmethod
    def states(i):
        ts = {1: 'семечко', 2: 'росток', 3: 'цветение', 4: 'зеленый', 5: 'спелый'}
        return ts[i]

    def grow(self):
        try:
            self._st += 1  # ate += 1
            return self._st
        except KeyError:
            print('роизошла ошибка, вероятно, этот томат уже созрел')

    def stet(self):  # возвращает стадию созревания
        return Tomato.states(self._st)

    def is_ripe(self):
        # """будет проверять, что томат созрел (достиг последней стадии созревания)"""
        return self._st  # ate == 'спелый'


class TomatoBush:
    def __init__(self, tomatoes_count):
        # """будет принимать в качестве параметра количество томатов и на его
        # основе будет создавать список объектов класса Tomato.Данный список будет храниться внутри
        # динамического свойства tomatoes."""
        self.tomatoes_count = tomatoes_count
        self.tomatoes_list = []
        self.states_list = []
        for i in range(tomatoes_count):
            self.st = random.randint(1, 5)
            print(self.st)
            # i = Tomato.states()[stt]
            Tomato(self.st)
            self.tomatoes_list.append(Tomato(self.st))
            self.states_list.append(self.st)
        # self._state = Tomato.states()[self.st]

    def stet(self):
        for i in self.states_list:
            print(Tomato.states(i))

    def grow_all(self):
        iterr = 0
        new_states_list = []  # """ будет переводить все объекты из списка томатов на следующий этап созревания"""
        for i in self.states_list:

            if i < 5:
                del self.tomatoes_list[iterr]
                self.tomatoes_list.append(Tomato(i + 1))
                new_states_list.append(i + 1)
                iterr += 1
            else:
                new_states_list.append(i)
                print('произошла ошибка, вероятно, этот томат уже созрел')
        self.states_list.clear()
        self.states_list += new_states_list

    def all_are_ripe(self):
        # """ будет возвращать True, если все томаты из списка стали спелыми"""
        list_ = []
        for object_ in self.states_list:
            list_.append(object_ == 5)
        if all(list_):
            return True
        else:
            return False

    def give_away_all(self):
        # """будет чистить список томатов после сбора урожая"""
        if self.all_are_ripe():
            self.tomatoes_list.clear()
            self.states_list.clear()
        else:
            inp = input('не все растения созрели, собрать урожай? да/yes для подтверждения: ')
            if inp == 'да' or inp == 'yes':
                self.tomatoes_list.clear()
                self.states_list.clear()

    def give_away_ripe(self):
        while 5 in self.states_list:
            for i in self.states_list:
                if Tomato.states(i) == 'спелый':
                    ii = self.states_list.index(i)
                    self.tomatoes_list.remove(self.tomatoes_list[ii])
                    self.states_list.remove(i)


class Gardener:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant

    def work(self):
        # """заставляет садовника работать, что позволяет растению становиться более зрелым"""
        self._plant.grow_all()

    def harvest(self):
        # """проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
        #  Если нет - метод печатает предупреждение."""
        if self._plant.all_are_ripe():
            print('собираем урожай')
            self._plant.give_away_all()
        else:
            print("еще слишком рано, не все плоды созрели!")

    @staticmethod
    def knowledge_base():
        """выведет в консоль справку по садоводству"""
        print("""справка по садоводству:
        work(self) - заставляет садовника работать, что позволяет растению становиться более зрелым
        harvest(self) - проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
         Если нет - метод печатает предупреждение.
         all_are_ripe(self) - соберет урожай только спелых кустов
         give_away_all(self) - соберет весь урожай
         all_are_ripe(self) - проверит все ли томаты спелые
         grow_all(self) - томаты переходят на следующую стадию созревания
         stet(self) - вернет стадии созревания всех томатов
        """)


'''1. Вызовите справку по садоводству
2. Ȅоздайте объекты классов TomatoBush и Gardener
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Ȃопробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Ȅоберите урожай'''

tomatos = TomatoBush(6)
gitter = Gardener('Gitter', tomatos)
gitter.knowledge_base()
tomatos.give_away_all()
print(tomatos.all_are_ripe())
tomatos.stet()
tomatos.grow_all()
tomatos.grow_all()
tomatos.grow_all()
tomatos.grow_all()
print(tomatos.all_are_ripe())
tomatos.give_away_all()
