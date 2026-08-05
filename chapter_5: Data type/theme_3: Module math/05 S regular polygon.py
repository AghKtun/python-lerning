# S regular polygon

from math import pi, pow, tan

n = int(input())
a = float(input())

S = (n * pow(a, 2)) / (4 * tan(pi / n))

print(S)
