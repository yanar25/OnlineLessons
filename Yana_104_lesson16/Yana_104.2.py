# Задача №1
# Пользователь будет вводить название и стоимость каждой
# своей покупки за день, до тех пор пока он не напишет
# “стоп”. Ваша задача записать это в json файл в формате:
# {"название" : "яблоко",
#  "стоимость": "200"}
import json


def shop(a):
    inp = {}

    while True:
        thing = input('продукт: ')
        if thing == 'стоп':
            break
        try:
            cost = int(input('цена: '))
        except ValueError:
            print('нужно ввести число!')
            continue
        inp[thing] = cost
    with open(f'{a}.json', 'w', encoding='utf-8') as hw:
        json.dump(inp, hw, ensure_ascii=False)


def cost_(a):
    cost = 0
    with open(f'{a}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for value in data.values():
            cost += int(value)
    return cost


shop('homework')

# Задача №2
# Прочитать файл из предыдущего задания и вывести
# стоимость всех покупок за день
print(cost_('homework'))
