# Sum of numbers 2

n = int(input())

total = 0

for i in range(1, n):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        total += i
        
print(total)
