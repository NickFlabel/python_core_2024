i = 1 # int -> 1.0
a = 2.5 # float
b = i + a
# print(b)

var = 0

# while var < 10:
#     print(var)
#     var += 1

while True:
    var += 1
    # Прервать выполнение цикла если
    # число достигло 10
    if var == 10:
        break
    print(var)

print("Вне цикла")

# break - ключевое слово при помощи
# которого мы можем покинуть
# цикл в любой момент времени

# continue - переход к следующей
# итерации цикла даже если код
# в теле цикла не был завершен

# i = 0
#
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue
#     print("Число было четным")


# Списки
# list
# Это структура данных, которая
# позволяет хранить упорядоченные
# коллекции данных.

numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "string", 1.5, True] # Списки могут хранить разные типы данных
my_var = "variable"
my_list = [my_var]
# Список объявляется при помощи [] и элементов
# перечисленных через запятую

# print(mixed_list)
# Чтобы достать какой-либо элемент
# списка мы можем обратится к нему
# через индекс
# <переменная со списком>[<индекс>]
print(mixed_list[0])
# Индексация элементов в списке
# начинается с нуля
# таким образом первый элемент
# списка в python будет иметь
# индекс 0, второй - 1,
# третий - 2 и так далее

#          0  1  2  3  4
my_list = [1, 2, 3, 4, 5]
# Индексация может быть обратной
# Для получения последнего элемента
# мы можем обратится к индексу -1,
# для второго с конца - -2 и так далее

print(my_list)
my_list.append(6) # метод append добавляет к списку то, что мы поместим в скобки
print(my_list)

# списки умеют реагировать на обычные операторы
list_1 = [1, 2]
list_2 = [3, 4]
list_3 = list_1 + list_2
print(list_3)

list_1 = [1, 2]
list_2 = [2, 3]
result = list(set(list_1) - set(list_2))
print(result)

# Лист можно умножать, но только на int
my_list = [1, 2]
my_list = my_list * 2
print(my_list)


my_list = ["old_string", "other_elements", 1]
# Замена первого элемента списка на какое-либо значение
my_list[0] = "new_string"
print(my_list)
# второй метод - для удаления значений
my_list.remove("other_elements")
print(my_list)

# Функция len() используется для определения длины какой-либо
# последовательности
len_of_list = len(my_list)
print("Длина списка: ", len_of_list)

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
    # if index == len(my_list):
    #     break

# my_list[0]
# my_list[1]
# my_list[2] -> IndexError - ошибка, сигнализирующая о том,
# что мы обратились к несуществующему индексу в каком-либо
# списке

for i in my_list:
    print(i)

# На первой итерации i = my_list[0]
# на второй итерации i = my_list[1]
# и так далее

# Итерация по всем элементам списка
for my_integer in range(1, 10, 2): # range - определение диапазона для значений my_integer
    print(my_integer)

# Пользователь вводит несколько чисел, которые надо добавить
# В список
# Затем программа должна посчитать сумму всех элементов

list_of_integers = [] # [1, 2]

while True:
    value = input("Введите число: ") # тип данных сохраняется как str
    if value == "q" or value == "Q":
        break
    value = int(value) # int(input())
    list_of_integers.append(value)

sum_of_lst: int = 0
for elem in list_of_integers:
    sum_of_lst += elem

print("Сумма всех элементов: ", sum_of_lst)

count = 0
for i in range(100, 1000):
    int_to_str = str(i) # не 100, а "100"
    if len(set(int_to_str)) == len(int_to_str):
        count += 1

print(count)

# Пользователь с клавиатуры вводит элементы списка
# целых чсисел. Необходимо подсчитать их сумму и их
# среднеарифметическое

list_of_numbers = []
while True:
    number = input("Введите число") # все что введет пользователь - строка
    if number == "end": # adaa
        break
    list_of_numbers.append(int(number))

sum_of_values = 0
for elem in list_of_numbers:
    sum_of_values += elem

result = sum_of_values / len(list_of_numbers)

print(result)
