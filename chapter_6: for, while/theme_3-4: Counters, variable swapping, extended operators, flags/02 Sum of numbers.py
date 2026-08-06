# Sum of numbers

n = int(input())    # вводим количество вводимых в последствии чисел

total = 0           # сумматор

for i in range(n):
    diff = int(input())
    total += diff
    
print(total)
