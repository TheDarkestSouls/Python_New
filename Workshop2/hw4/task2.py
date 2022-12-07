# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# *Пример*

# - при N=236     ->        [2, 2, 59]

num = int(input("Enter the number: "))
multList = []
while num % 2 == 0:
    num //= 2
    multList.append(2)
while num % 3 == 0:
    num //= 3
    multList.append(3)
else:
    if not num == 1:
        multList.append(num)
print(multList)