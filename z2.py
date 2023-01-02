# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for w in range(2):
    for y in range(2):
        for z in range(2):
            for x in range(2):
                if (w and z) or not y or (not x == (not w)):
                    print(f'Утверждение (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) истинно при w = {w}, y={y}, z={z},x={x}')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# if not (x or y or z) == (not x and not y and not z):

#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            if not (x or y or z) == (not x and not y and not z):
#                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истенно при x = {x}, y={y}, z={z}')