# Dog age

age_dog = int(input())

if age_dog < 3:
    age_dog_in_human = age_dog * 10.5
    print(age_dog_in_human)
else:
    age_dog_in_human = (age_dog - 2) * 4 + 21
    print(age_dog_in_human)
