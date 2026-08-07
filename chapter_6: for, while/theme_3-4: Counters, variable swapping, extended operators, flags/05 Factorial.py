# Factorial

# решение через math
from math import factorial

n = int(input())

F = factorial(n)

print(F)


# решение через цикл for
n = int(input())

total = 1

for i in range(1, n + 1):
    total *= i

print(total)
