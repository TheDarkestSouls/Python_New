# # Lection 3

# def f(x):
#     x**2
# g = f
# print(f(1)) #same result
# print(g(1)) #same result

########################################

# def f(x):
#     return x**2
# g = f
# print(f(4)) #class function
# print(g(4)) #class function

########################################

# def calc1(x):
#     return x+10
# print(calc1(10))

# def calc2(x):
#     return x*10
# print(calc2(10))

# def math(op, x): # function as an argument
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

########################################

# # Lambda

# # def sum(x, y):
# #     return x+y
# # or...
# sum = lambda x, y: x+y

# # def mult(x, y):
# #     return x*y
# # or...
# mult = lambda x, y: x*y

# def calc(op, a, b): # function as an argument
#     print(op(a, b))
#     # return op(a, b)

# # calc(mult, 4, 5) # using function
# # calc(sum, 4, 5) # using lambda
# # or ...
# calc(lambda x, y: x*y, 4, 5) # using lambda as an argument
# calc(lambda x, y: x+y, 4, 5) # using lambda as an argument

########################################

# List comprehensions

list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)
# or...
# list = [i for i in range(1, 21)]             # simple
# print(list)
# list = [i for i in range(1, 21) if i % 2 == 0] # with condition
# print(list)
# list = [(i, i) for i in range(1, 21) if i % 2 == 0] # with condition and tuples
# print(list)
# def f(x):
#     return x**3
# list = [f(i) for i in range(1, 21) if i % 2 == 0] # with condition and function
# print(list)
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # with condition, tuples and function
# print(list)

# Task(my result):

# def f(x):
#     return x**2
# list = [1,2,3,5,8,15,23,38]
# list1 = [(i, f(i)) for i in list if not i % 2]
# print(list1)

# Task(from lection):

path = 'C:\Users\NikEli\Desktop\GeekBrains\Python\FirstSteps\file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)

