# S and C circle

from math import pi, pow

R = float(input())

S = pi * pow(R, 2)
C = 2 * pi * R

print(S, C, sep='\n')
