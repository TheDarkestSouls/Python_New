# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

our_list = [1.1, 1.2, 3.1, 5, 10.01]

min = our_list[0] % 1
max = our_list[1] % 1

for i in our_list:
    if i % 1 <= min:
        min = i
    if i % 1 >= max:
        max = i

print(max % 1 - min % 1)
    