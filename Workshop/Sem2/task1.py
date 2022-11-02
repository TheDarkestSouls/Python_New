# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# number = input()
# sum = 0
# for i in number:
#     if i == ',':
#         continue
#     sum += int(i)
# print(sum)

number = input()
number = [int(i) for i in number if i.isnumeric()]
print(sum(number))


