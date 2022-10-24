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