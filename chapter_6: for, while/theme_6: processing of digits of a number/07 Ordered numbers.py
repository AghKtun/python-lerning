# Ordered numbers

num = int(input())

len_num = len(str(num))

digit_n = num % 10
Flag = 'YES'
counter = 0

while num > 0:
    digit_m = num % 10
    
    if digit_m >= digit_n:
        counter += 1
       
    if counter == len_num:
        Flag = 'YES'
    else:
        Flag = 'NO'
        
    digit_n = digit_m
    num //= 10
    
print(Flag)
