# Реализуйте алгоритм перемешивания списка.


import random
list = ['a','b','c','d','e','f','g']
new_list = []
while len(list) > 0:
    r = random.choice(list)
    new_list.append(r)
    list.remove(r)
list = new_list
print(list)

# !!!OR SIMPLY!!!:
# list = ['a','b','c','d','e','f','g']
# random.shuffle(list)
# print(list)