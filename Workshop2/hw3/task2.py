# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pair_product_list(list):
    new_list = []
    for i in range(len(list)):
        if i < len(list) / 2:
            new_list.append(list[i] * list[-(i + 1)])
        else:
            break
    return new_list


list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

print(pair_product_list(list1))
print(pair_product_list(list2))
