# The second digit

num = int(input())

counter_digit = len(str(num))

second_digit = (num // 10 ** (counter_digit - 2)) % 10

print(second_digit)
