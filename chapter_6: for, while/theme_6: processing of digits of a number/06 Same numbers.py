# Same numbers

num = int(input())

if num % 10 == 0:
    print('NO')
else:
    counter_digit = len(str(num))
    digit = num % 10
    
    if num // digit == int(counter_digit * '1'):
        print('YES')
    else:
        print('NO')
