# max and min

num = int(input())

max_digit = 0
min_digit = 9

while num != 0:
    laster_digit_num = num % 10
    num //= 10
    maxmin_digit = laster_digit_num 
    if laster_digit_num > max_digit:
        max_digit = laster_digit_num    
    if laster_digit_num < min_digit:
        min_digit = laster_digit_num

print('Максимальная цифра равна ', max_digit, '\n', 'Минимальная цифра равна ', min_digit, sep='')
