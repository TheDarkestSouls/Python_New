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


# Lection 2

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w') # w - rewrite 
# data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close

# with open('file.txt', 'a') as data: # a - add
#     data.write('LINE 1\n')
#     data.write('LINE 2\n')

# path = 'file.txt'
# data = open(path, 'r') # r - read
# for line in data:
#     print(line)
# data.close()

# exit()

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))

# def concatinatio(*params):
#     res: str = ""
#     for items in params:
#         res += items
#     return res

# print(concatinatio('a','s','d','w'))
# print(concatinatio('a','1'))

# def concatinatio(*params):
#     res = 0
#     for items in params:
#         res += items
#     return res

# print(concatinatio(1, 2, 3, 4))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Tuples

# a = (1, 2, 3, 4)
# print(a[0]) # 1 element
# print(a[-1]) # last element
# print(a[-2]) # before last element etc
# # a[0] = 12 # error
# for item in a: # 1 2 3 4
#     print(item)

# t = tuple(['red', 'green', 'blue']) # convert list to tuple
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# Dictionaries

# dictionary = {}
# # use \ to start with a new line
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left']) # ←

# # for k in dictionary.keys(): # to show keys
# #     print(k)
# # for k in dictionary.values(): # to show values
# #     print(k)
# # for v in dictionary: # to show keys var2
# #     print(v)
# # for v in dictionary: # to show values var2
# #     print(dictionary[v])

# print(dictionary['up']) # rename
# dictionary['up'] = 'up'
# print(dictionary['up'])

# ====================

# colors = {'red', 'green', 'blue'}

# print(type(colors)) # <class 'set'>
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'gray', 'green', 'blue'}
# colors.remove('red')
# print(colors) # {'blue', 'gray', 'green'}
# # colors.remove('red') # error
# colors.discard('red') # ok
# print(colors)
# colors.clear() # emptying
# print(colors) # set()

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()            # c = a = {1,2,3,5,8}
# u = a.union(b)          # u = a + b = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   # i = {8, 2, 5}
# dl = a.difference(b)    # dl = {1, 3}
# dr = b.difference(a)    # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1,21,3,13}

# s = frozenset(a) # const set



# Little bit more about lists

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e) # 1 2 3 4 5

# print()

# for e in list2:
#     print(e) # 1 2 3 4 5

# print()
# list1[0] = 55 # change 1 element of list1

# for e in list1:
#     print(e) # 55 2 3 4 5

# print()

# for e in list2:
#     print(e) # 55 2 3 4 5

# print()
# list2[1] = 77 # change 2 element of list2

# for e in list1:
#     print(e) # 55 77 3 4 5

# print()

# for e in list2:
#     print(e) # 55 77 3 4 5


# list1 = [1,2,3,4,5]
# print(list1.pop())         # cut last element off
# print(list1)
# print(list1.pop(3))        # cut specific element off
# print(list1)       
# print(list1.insert(2, 35)) # insert specific element in selected position
# print(list1)
# print(list1.append(86))    # insert specific element in the last position
# print(list1)








