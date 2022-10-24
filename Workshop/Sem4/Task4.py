# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Enter power degree: "))
while k >= 0:
    if k > 1:
        print(f'{random.randint(1, 100)}x^{k}', end = '+')
    k -= 1
    if k == 0:
        print(random.randint(1, 100))
        


