# Calculator

a = int(input())
b = int(input())
operator = input()

if operator == "+":
    n = a + b
    print(n)
elif operator == "-":
    n = a - b
    print(n)
elif operator == "*":
    n = a * b
    print(n)
elif operator == "/" and b != 0:
    n = a / b
    print(n)
elif operator == "/" and b == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')
