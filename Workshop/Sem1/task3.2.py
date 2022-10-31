# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21



Ax = int(input("Enter Ax coordinates: "))
Ay = int(input("Enter Ay coordinates: "))
Bx = int(input("Enter Bx coordinates: "))
By = int(input("Enter By coordinates: "))
print("Distance beetween A and B is ", round(((Ax - Bx)**2 + (Ay - By)**2)**0.5, 2))