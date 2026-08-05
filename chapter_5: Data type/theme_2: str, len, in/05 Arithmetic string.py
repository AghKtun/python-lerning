# Arithmetic string

string_1 = input()
string_2 = input()
string_3 = input()

length_string_1 = len(string_1)
length_string_2 = len(string_2)
length_string_3 = len(string_3)

min_string = min(length_string_1, length_string_2, length_string_3)
max_string = max(length_string_1, length_string_2, length_string_3)
middle_string = length_string_1 + length_string_2 + length_string_3 - min_string - max_string

if 2 * middle_string == min_string + max_string:
    print('YES')
else:
    print('NO')
