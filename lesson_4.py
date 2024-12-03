# Области видимости

# Областью видимости в Python называется область в коде,
# где можно использовать ту или иную переменную и кто
# имеет к ней доступ

x = 1 # Глобальная переменная x

def my_func():
    x = 10 # Локальная переменная x, относящаяся к my_func
    print(x)

# my_func() # 10
# print(x) # 1

# Локальная область видимости
# Это переменные, объявленные внутри функции
# и доступные только внутри этой функции

def my_func_2():
    y = 10 # my_func_2_y
    return y

# Глобальные переменные
# Глобальной переменной называется переменная,
# объявленная в модуле и доступная из любого его места

global_var = "global"

def example_global():
    global global_var
    global_var = "new global"

example_global()

print(global_var)
# При помощи ключевого слова global можно использовать
# глобальные переменные внутри функции

# Встроенная область видимости
print() # функция print является частью встроенной области
# видимости
# int()
# float()
# len()

# Встроенная область видимости - функции и переменные,
# которые доступны в python по умолчанию без
# необходимости что-либо импортировать или объявлять

# Shadowing - переопределение переменных
# Локальные переменные могут "закрывать" глобальные или
# встроенные
# len = 42
# print(len)

# Внутренние функции в Python
# Внутренние функции - это функции, определенные внутри
# другой функции

def outer_function(name):
    def inner_function():
        print(f"Hello, {name}")
    inner_function()

outer_function("test") # Python вызовет inner_function
# при вызове outer_function

# Внутренние функции полезны для изоляции
# вспомогательных операций

def process_data(data):
    def clean_data(d):
        return [item.strip() for item in d]

    cleaned = clean_data(data)
    return cleaned

# Фабрика функций
# Необходимо много раз возвести разные числа в какую-либо
# степень

def make_multiplier(factor):
    def multiplier(x):
        return x ** factor # 2
    return multiplier # Возврат функции как переменной

to_power_two = make_multiplier(2) # to_power - функция
to_power_three = make_multiplier(3)
to_power_four = make_multiplier(4)
print(to_power_two(2))
print(to_power_three(2))
print(to_power_four(2))

# Замыкание

# Замыкающая область - переменная определена в окружающих
# функциях, но не в глобальных

def outer():
    x = 1 # перменная, локальная для outer()
    def inner():
        nonlocal x # получение доступа к переменной из
        # внешней функции outer
        x += 1

# Напишите функцию process_text, которая принимает
# какой-либо текст и содержит внутреннюю функцию,
# превращающую все знаки текста в большие буквы
# (.upper())

def process_text(text):
    def to_upper(t):
        return t.upper()
    return to_upper(text) # уже увеличенный текст

text = "lower_case_text"
print(process_text(text))

# Рекурсия
# Рекурсивные функции - это функции, которые
# вызывают сами себя во время вополнения для решения
# задачи, разбивая ее таким образом на меньшие подзадачи

# Основные элементы рекурсивной функции
# 1) Базовый случай
# 2) Рекурсивный случай

def factorial(n): # 0
    # Базовый случай
    if n == 0:
        return 1
    # Рекурсивный случай
    else:
        return n * factorial(n-1)

# Вычисляем факториал тройки
# 1 - 3 * factorial(2) = 3 * 2
# 2 - 2 * factorial(1) = 2 * 1
# 3 - 1 * factorial(0) = 1 * 1
# 4 - 1
#
# print(factorial(-3))

# Числа Фибоначчи - последовательность чисел,
# где два последних числа при сложении составляют
# следующее число последовательности

fib = [1, 1, 2, 3, 5, 8, 13]

# Задача - написать функцию, которая при прокидывании
# в нее целого числа n будет вычислять n-ое число
# поледовательности Фибоначчи

def fibonacci(n): # 8
    # Базовый случай - fibonacci(1)
    if n <= 1:
        return n
    # Рекурсивный случай - fibonacci(50)
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    # fibonacci(7) + fibonacci(6)
    # fibonacci(6) + fibonacci(5)
    # fibonacci(5) + fibonacci(4)
    # fibonacci(4) + fibonacci(3)
    # fibonacci(3) + fibonacci(2) = 3 + 2 = 5
    # fibonacci(2) + fibonacci(1) = 1 + 1 = 2
    # fibonacci(1) + fibonacci(0) = 1 + 0 = 1

print(fibonacci(8))

