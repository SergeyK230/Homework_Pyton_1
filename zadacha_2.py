# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in True, False:
    for y in True, False:
        for z in True, False:
            itog = not(x or y or z) == (not x and not y and not z)
            print('x = {}  y = {}  z = {}  -> {}'.format(x, y, z, itog))
