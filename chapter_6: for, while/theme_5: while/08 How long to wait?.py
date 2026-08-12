# How long to wait?

# первый метод решения, который пришел в голову через два while
name = input()

counter = 0

while 'Александра' not in name:
    name = input()

name = input()

while 'Левон' not in name:
    counter += 1
    name = input()

print(counter)

# второе решение через флаг
name = input()

counter = 0
flag = False    # флаг для имени 'Александра' - пора запускать счетчик

while 'Левон' not in name:
    
    if name == 'Александра' and flag == False:
        flag = True
    elif flag == True:
        counter += 1  
        
    name = input()

print(counter)
