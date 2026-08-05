# Roulette wheel color

x = int(input())

if 0 <= x <= 36:
    if x == 0:
        print('зеленый')
    elif ((1 <= x <= 10 or 19 <= x <= 28) and x % 2 == 0) or ((11 <= x <= 18 or 29 <= x <= 36) and x % 2 != 0):
        print('черный')
    elif ((11 <= x <= 18 or 29 <= x <= 36) and x % 2 == 0) or ((1 <= x <= 10 or 19 <= x <= 28) and x % 2 != 0):
        print('красный')
else:
    print('ошибка ввода')
