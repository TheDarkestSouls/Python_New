# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from operator import index
import random
# list = []
# l = int(input("enter the length of a list: "))
# for i in range(1, l+1):
#     list.append(random.randint(1,9)) # list = [x, x, x.....x]
# print(list)
# print()

# LN = 1
# for i in range(0, len(list)):
#     if i < len(list)/2:
#         print(list[i] * list[-LN])
#         LN += 1

num_list = [random.randint(1, 9) for i in range(1, int(input("Enter the amount of symbols: "))+1)]
print(num_list, " => ", [num_list[i]*num_list[-(i+1)] for i in range(int(len(num_list)) - int(len(num_list)/2))])


    







