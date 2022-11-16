# Домашнее задание
# ȃеализуйте итератор колоды карт (52 штуки) CardDeck.
# Каждая карта представлена в виде строки типа «2 Ȃик».
# Ȃри вызове функции next() будет представлена
# следующая карта. Ȃо окончании перебора всех
# элементов возникнет ошибка StopIteration.


class CardDeck:
    def __init__(self):

        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'В', 'Д', 'К', 'А']
        self.suit = ['пика', 'креста', 'бубна', 'черва']
        self.cards = [str(j) + ' ' + i for i in self.suit for j in self.deck]
        self.map_index = 0

    def __iter__(self):
        self.card = ''
        return self

    def __next__(self):
        try:
            self.card = self.cards[self.map_index]
            self.map_index += 1
            return self.card
        except StopIteration:
            print('hhh')


a = CardDeck()

e = iter(a)
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
print(e.__next__())
