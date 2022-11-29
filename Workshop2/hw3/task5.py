# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [-1, 1, 2]:
        return 1
    elif n == -2:
        return -1
    else:
        return fib(n-1) + fib(n-2)

k = int(input())

list1 = []
list2 = []
for e in range(1, k+1):
    list1.append(fib(e))
for f in range(0, k+1):
    if not f%2:
        list2.append(fib(f) * -1)
    else:
        list2.append(fib(f))

print(list(reversed(list2)) + list1)
