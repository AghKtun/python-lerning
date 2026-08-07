# Asymptotic approximation

from math import log

n = int(input())
m = 0

for i in range(n):
    m += 1 / (i + 1)

diff = m - log(n)
print(diff)
