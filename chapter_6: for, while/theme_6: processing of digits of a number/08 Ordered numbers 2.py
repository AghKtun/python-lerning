# Ordered numbers 1

num = int(input())

len_num = len(str(num))
counter = 0

for i in range (1, len_num + 1):
    digit = num // 10 ** (len_num - i) % 10
    
    if digit % 2 == 0:
        counter += 1
        print(counter, '-я', ' четная цифра равна ', digit, sep='')
    
if counter == 0:
    print('Четных цифр в числе нет')
