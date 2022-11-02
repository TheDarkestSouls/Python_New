# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. (1+1/n)**n

# Пример:

# Для n = 6: [2,2,2,2,2,3] -> 13

# list = []
# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     list += str(round(((1+1/i)**i)))
# for j in list:
#     sum += int(j)
# print(list, '->', sum)

n = int(input())
list = [round((1+1/i)**i) for i in range(1, n+1)]
print(list, " -> " , sum(list))