# Вычислить число π c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

i = int(input())
while 10 < i < 1:
    i = int(input())
else:
    print(round(math.pi, i))