# user_input = input("Введите слова через пробел")
# my_list = user_input.split(" ")
# print(my_list)

user_input = input("Введите строку:")
number_of_digits = 0
number_of_letters = 0

for elem in user_input:
    if elem.isalpha(): # isalpha() - True если символ - буква
        number_of_letters += 1
    if elem.isdigit():
        number_of_digits += 1

print("Количество букв: ", number_of_letters)
print("Количество цифр: ", number_of_digits)