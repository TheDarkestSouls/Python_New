# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = int(input("Enter the number: "))
n = ""
while x > 0:
    y = str(x%2)
    n = y + n
    x = int(x/2)
n = int(n)
print(n)

    
    




