# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

i = int(input())
while i<1 or i>10:
    i = int(input())
else:
    print(round(math.pi, i))


