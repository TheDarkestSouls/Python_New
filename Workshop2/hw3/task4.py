# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec = int(input())
bin = ''

if dec == 0:
    bin = int(0)
    print(bin)
else:
    while dec // 2 > 0:
        bin = str(dec % 2) + bin
        dec //= 2
    print(int('1' + bin))
