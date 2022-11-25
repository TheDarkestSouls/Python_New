# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

n = int(input())
seq = []
sum = 0

for i in range(1, n + 1):
    seq.append((1 + 1 / i) ** i)
    sum += (1 + 1 / i) ** i
    
print(f'{seq}, ->, {sum}')