# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


nums = list(map(int, input().split()))
print(nums)
new_nums = []
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
print(new_nums)