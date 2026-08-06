# Population

m = int(input())    # стартовое количество организмов
p = int(input())    # среднесуточное увеличение в %
n = int(input())    # количество дней для размножения

for i in range(n):
        diff = m * pow(1 + p / 100, i)    # решается  через сложный процент
        print(i + 1, diff)
