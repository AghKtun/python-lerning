# Number of members

word = input()

counter = 0

while not (word == 'стоп' or word == 'хватит' or word == 'достаточно'):
    counter += 1
    word = input()

print(counter)
