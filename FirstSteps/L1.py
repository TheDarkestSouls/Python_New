from calendar import c
from cgitb import text
from importlib.resources import path
from msilib.schema import Condition
from multiprocessing.sharedctypes import Value
from operator import invert, truediv
from re import S, T

# Lection 1

# value = None
# # print(value)
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))

# value = 1234
# print(value)

# s = 'hello "world"'
# print(s) # output line
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b ,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)
# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5, True]
# print(list)
# print(col)

# print('Enter a');
# a = float(input())
# print('Enter b');
# b = float(input())
# print(a, '+', b, ' ', '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# a = 1.433425425
# b = 3
# c=round(a*b, 7)
# print(c)

# a = 3
# a += 5
# print(a)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Enter your name: ')
# if username == 'Liza':
#     print('Im glad you re here, Liza!=D')
# elif username == 'Nikita':
#     print('Hello Nikita!')
# else:
#     print('Hi ', username)

# original = 345
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 345
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Its')
#     print('enough')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in range(10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwerty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'


# help(str)

# print(len(text))                 # 39
# print('еще' in text)             # True
# print(text.isdigit())            # False
# print(text.islower())            # True
# print(text.replace('еще','ЕЩЕ')) #

# print(text[0])
# print(text[1])
# print(text[len(text)])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[2:5])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]

# numbers = [1,2,3,4,5]
# print(numbers)                # [1,2,3,4,5]
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)                #  1,2,3,4,5
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                #  [10,2,3,4,5]
# for i in numbers:
#     i *= 2
#     print(i)                  # [20,4,6,8,10]
# print(numbers)                # [10,2,3,4,5]

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)       # red green blue
# for e in colors:
#     print(e*2)     # redred greengreen blueblue

# colors.append('gray') # add to the end
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') # del colors[0] # delete element




# def function_name(x):
#     # body line 1
#     # . . .
#     # body line n
#     # optional return


# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# arg = 0
# print(f(arg))
# print(type(f(arg)))

