# Interesting number

n = int(input())

a = n // 100
b = n % 100 // 10
c = n % 10

digit_max = max(a, b, c)
digit_min = min(a, b, c)
digit_middle = (a + b + c) - digit_max - digit_min

if  digit_max - digit_min == digit_middle:
    print('Число интересное')
else:
    print('Число неинтересное')
