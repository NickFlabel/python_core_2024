# Срез списка (slice)
# Срез списка в Python позволяет извлекать подсписки
# из оригинального списка, указав диапазон индексов

# Основной синтаксис среза: list[начало:конец:шаг]

lst = [10, 20, 30, 40, 50, 60, 70] # -> [20, 30, 40]
# Моя задача - получить все значения с индексами 1, 2, 3
slice1 = lst[1:4] # [20, 30, 40]
slice2 = lst[:] # полный список
slice3 = lst[::2] # [10, 30, 50, 70]
slice4 = lst[-3:-1] # [50, 60]
slice5 = lst[::-1] # [70, 60 ...]
slice6 = lst[3:] # [40, 50, 60, 70]
slice7 = lst[:3] # [10, 20, 30]

# Генерация списков или list comprehension

# Синтаксический сахар

for i in range(1, 5):
    lst.append(i)

# Генераторы списков - синтаксический сахар, позволяющий
# эффективно создавать новые списки, применяя выражения
# и условия в компактной и читаемой форме

# [выражение for элемент in список if условие]

lst = [1, 2, 3, 4, 5]

result = []
for elem in lst:
    result.append(elem*elem)

result = [elem*elem for elem in lst] # тоже самое что строки 32-34
# [выражение for элемент in список if условие]

# Реализация через обычный цикл
result = []
for elem in lst:
    if elem % 2 == 0:
        result.append(elem)

# Реализация при помощи генерации списка
result = [elem for elem in lst if elem % 2 == 0]

# Методы list

# append(x: Any) -> добавляет элемент x в конец списка
# extend(x: list) -> расширяет первый список добавляя
# все элементы из списка x в конце оригинального списка
lst = [1, 2, 3]
lst2 = [4, 5, 6]
new_list = lst + lst2 # [1, 2, 3, 4, 5, 6]
lst.extend(lst2) # -> [1, 2, 3, 4, 5, 6]
# insert(i: int, x: Any) - вставляет x на индекс i
lst.insert(2, 'НОВОЕ ЗНАЧЕНИЕ')
# remove(x: Any) - удаляет первый элемент со значением x
# pop(i: int) - удаляет элемент с индексом i, метод возвращает
# это значение
pop_result = lst.pop(2) # "НОВОЕ ЗНАЧЕНИЕ"
lst = [1, 2, 3, 4, 5]
my_val = lst.pop() # my_val = 5, lst = [1, 2, 3, 4]
my_val = lst.pop(1) # my_val = 2, lst = [1, 3, 4, 5]
# sort() - сортирует элементы списка
unsorted_list = [100, 8, 56, 44, 42]
unsorted_list.sort() # [8, 42, 44, 56, 100]
unsorted_list.sort(reverse=True) # [100, 56, 44, 42, 8]
# reverse() - переворачивает порядок элементов

# Строки (str)

long_text = """
При помощи трех кавычек мы можем 
написать длинный str, который будет
занимать больше одной строки
"""

str1 = "первая строка"
str2 = "вторая строка"

# Сложение списков
str3 = str1 + str2 # При помощи оператора + мы
# можем создавать новые списки, состоящие из слагаемых

# Умножение списков
str4 = "a"
str5 = str4 * 3
print(str5)

# f-строка
name = "test_name"
age = 30
str6 = f"Имя: {name}, возраст: {age}"

# join - объединение элементов списка-строк в отдельную строку
# элементы которой разделены строкой, на которую вызывается метод
# join()
words = ["first_word", "second_word", "third_word"]
sentence = " ".join(words)

# split(x: str) - разделяет строку используя в качестве
# разделителя x
my_str = "first,second,third"
my_list = my_str.split(",") # ["first", "second", "third"]

# Индексация в строках
my_str = "my string"
my_str[1] # "y"
# На строках работают срезы точно также как они работали на
# списках
my_str[1:4] # "y s"

# Методы в строках

# Изменения в регистре
# .upper() - переводит строку в верхний регистр
my_str = "lower_case_str"
print(my_str.upper())
# .lower() - переводит строку в нижний регистр
# .capitalize() - делает первую букву строки заглавной

# Поиск и проверка
# .find(x: str) -> возвращает индекс первого появления подстроки
# или -1 если подстрока не найдена
main_str = "my_main_str"
str_to_be_found = "main"
index = main_str.find(str_to_be_found) # 3 - индекс с которого
# начинаетсся слово main

# .index(x: str) - делает тоже самое, что find, но при неудаче
# он вызывает ошибку

# replace(old: str, new: str) - меняет все подстроки old на
# строку new
text = "my_old_old_str"
print(text.replace("old", "new"))

# Удаление пробелов и символов
# .strip() - удаляет пробелы с начала и конца строки
my_username = "test_username   "
new_username = my_username.strip()
print(new_username + "|")

# .lstrip() - left - удаляет пробелы слева
# .rstrip() - right - удаляет пробелы справа

# .isalpha() - возвращает True если строка состоит из букв
# .isdigit() - возвращает True если строка состоит из цифр


