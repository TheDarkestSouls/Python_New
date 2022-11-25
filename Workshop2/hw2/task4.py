# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

N = int(input('Enter a number: '))

great_list = []
for i in range(-N, N+1):
    great_list.append(i)
print(great_list)

el_1 = great_list[int(input('multiplicand is: '))]
el_2 = great_list[int(input('multiplier is: '))]

print(f'product is: {el_1 * el_2}')

