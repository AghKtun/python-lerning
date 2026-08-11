# Number of fives

num = int(input())

counter = 0

while not (num <= 0 or num > 5):
    if num == 5:
        counter += 1
    num = int(input())

print(counter)
