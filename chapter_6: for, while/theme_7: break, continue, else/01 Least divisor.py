# Least divisor

n = int(input())

len_n = len(str(n))

for i in range(2, n + 1):   
    if n % i == 0:
        print(i)
        break
