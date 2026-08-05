# Three sity

city_1 = input()
city_2 = input()
city_3 = input()

length_city_1 = len(city_1)
length_city_2 = len(city_2)
length_city_3 = len(city_3)

max_len = max(length_city_1, length_city_2, length_city_3)
min_len = min(length_city_1, length_city_2, length_city_3)
    
if length_city_1 == min_len:
    print(city_1)
elif length_city_2 == min_len:
    print(city_2)
elif length_city_3 == min_len:
    print(city_3)

if length_city_1 == max_len:
    print(city_1)
elif length_city_2 == max_len:
    print(city_2)
elif length_city_3 == max_len:
    print(city_3)
