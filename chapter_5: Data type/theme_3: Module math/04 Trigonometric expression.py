# Trigonometric expression

from math import radians, sin, cos, tan, pi

x = float(input())
x_rad = radians(x)
trigonometric = sin(x_rad) + cos(x_rad) + pow(tan(x_rad), 2)

print(trigonometric)
