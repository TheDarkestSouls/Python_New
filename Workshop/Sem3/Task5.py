# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    if n in [-1, 1, 2]:
        return 1
    elif n == -2:
        return -1
    else:
        return fib(n-1) + fib(n-2)

# num = int(input())
# l1 = [fib(f) * ((-1)**(fib(f)+1)) for f in range(0, num+1)]
# l2 = [fib(e) for e in range(1, num+1)]
num = int(input())
fib_list = []
for e in range(1, num+1):
    fib_list.append(fib(e))
for f in range(0, num+1):
    fib_list.insert(0, fib(f) * ((-1)**(fib(f)+1)))
# print(list(reversed(l1)) + l2)
print(fib_list)


