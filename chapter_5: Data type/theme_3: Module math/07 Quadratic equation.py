# Quadratic equation

from math import sqrt

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D > 0:
    x_1 = (-b - sqrt(D)) / (2 * a)
    x_2 = (-b + sqrt(D)) / (2 * a)
    min_root = min(x_1, x_2)
    max_root = max(x_1, x_2)
    print(min_root, max_root, sep='\n')
elif D == 0:
    x = -(b / (2 * a))
    print(x)
else:
    print('Нет корней')
