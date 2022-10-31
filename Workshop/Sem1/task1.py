# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input())
# if day == 6 or day == 7:
#     print("Yes")
# else:
#     print("No")

weekend = int(input())
if 5 < weekend < 8:
    print("Yes")
else:
    print("No")

    

