# number of coins

price = int(input())

caunter_coins = 0

th25 = price // 25
th10 = price % 25 // 10
th5 = price % 25 % 10 // 5
th1 = price % 25 % 10 % 5 // 1
caunter_coins = th25 + th10 + th5 + th1

print(caunter_coins)
