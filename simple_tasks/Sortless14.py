from random import random

# Создание случайного списка
def make_list():
    list = []
    for i in range(50):
        list.append(int(random() * 30))
    return list


li = make_list()

# Список до преобразования
print("before: ", li)

# Список после преобразования
print("after: ", sorted([x for x in li if x > 14], reverse=True))
