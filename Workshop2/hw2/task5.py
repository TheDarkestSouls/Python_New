# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random

old_list = [1, 2, 3, 4, 5]
new_list = []

while len(old_list) > 0:
    rnd = old_list[random.randint(0, len(old_list) - 1)]
    new_list.append(rnd)
    old_list.remove(rnd)

print(new_list)
