# Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [2.35, 1.02, 15.87, 9.23, 7.15] # My example

list = [1.1, 1.2, 3.1, 5, 10.01]         # Sergey example
# max = list[0]%1
# min = list[1]%1
# for i in list:
#     if i%1 > max:
#         max = i%1
# for j in list:
#     if j%1 < min:
#         min = j%1
# print(max - min)

li = sorted([int(i%1*100)/100 for i in list])
print(li[-1] - li[0])



