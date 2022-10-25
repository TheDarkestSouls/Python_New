# Создайте программу для игры в ""Крестики-нолики"".
from random import randint
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

win = (['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['a', 'd', 'g'], [
       'b', 'e', 'h'], ['c', 'f', 'i'], ['a', 'e', 'i'], ['c', 'e', 'g'])

print('\n', a, '|', b, '|', c, '\n-----------', '\n', d, '|',
      e, '|', f, '\n-----------', '\n', g, '|', h, '|', i, '\n')

go_first = int(randint(1, 2))

p1 = []
p2 = []

while win:
    if go_first == 1:
        go_first = 2
        p1.append(input('\nWhich position do you want to put X on? '))
        p1.sort()
        if p1 in win:
            print(p1, "P1 wins!")
            win = 0
    else:
        go_first = 1
        p2.append(input('\nWhich position do you want to put O on? '))
        p2.sort()
        if p2 in win:
            print(p2, "P2 wins!")
            win = 0
