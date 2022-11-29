# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

list1 = []
sum = 0

for i in range(int(input('length of list: '))):
    list1.append(randint(1, 9))

for i in range(1, len(list1), 2):
    sum += list1[i]

print(list1)
print(sum)
