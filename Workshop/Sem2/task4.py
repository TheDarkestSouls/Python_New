# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


N = int(input())
list = []
result = int(1)
for i in range(-N, N + 1):   # make list
    if i == 0:
        continue
    list.append(i)
print(list)

path = 'file.txt'
data = open(path, 'r')
for num in data:             # multiple its elements with indices specified in file.txt
    result *= list[int(num)]
    print(list[int(num)])
print(result)
