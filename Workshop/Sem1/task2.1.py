# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# not (X or Y or Z) = not X and not Y and not Z

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if not (X or Y or Z):
                print(not X and not Y and not Z)
