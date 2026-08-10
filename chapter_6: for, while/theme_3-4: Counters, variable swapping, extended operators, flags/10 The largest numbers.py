# The largest numbers

n = int(input())

num1 = int(input())
num2 = int(input())

if num1 > num2:
    max1 = num1
    max2 = num2
else:
    max1 = num2
    max2 = num1

for _ in range(n - 2):
    current = int(input())
    if current > max1:
        max2 = max1
        max1 = current
    elif current > max2:
        max2 = current

print(max1, max2, sep='\n')
