# All in one

num = int(input())

counter_digit = len(str(num))

total_sum = 0
total_mul = 1
total_digit_f_e = 0
first_digit = 0

for i in range(1, counter_digit + 1):
    digit = num % 10
    total_sum += digit
    total_mul *= digit
    if i == 1:
        total_digit_f_e += digit
    if num // 10 == 0:
        total_digit_f_e += digit
        first_digit += digit
    num //= 10 

arithmetic = total_sum / counter_digit

print(total_sum, counter_digit, total_mul, arithmetic, first_digit, total_digit_f_e, sep='\n')
