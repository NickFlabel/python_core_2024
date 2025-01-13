# Декораторы
# @декоратор
# def func():

# Паттерны проектирования - типовые решения
# часто встречающихся проблем

# Декоратор в широком смысле - паттерн
# проектирования

# В программировании есть следующий принцип -
# open/close или принцип открытости/закрытости

def my_func():
    return "Hello"

# Декоратор "оборачивает" какой-либо модуль
# нашей программы для модификации его поведения

print(my_func()) # Hello
print(my_func)

def world(func):
    print(func(), "World")

world(my_func)

# Декоратор в узком смысле - это функция в python, которая
# принимает в качестве аргумента другую функци и возвращает
# новую функцию, которая расширяет или изменяет поведение
# оригинальной функции

def multiplication(multiplier):
    def inner_func(a):
        return a * multiplier
    return inner_func

my_mult_func = multiplication(5)
print(my_mult_func(2))

def world_decorator(func): # func = my_func
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # "Hello"
        result = result + " World"
        return result
    return wrapper

# decorated_func = world_decorator(my_func)
# print(decorated_func)
# print(decorated_func())

@world_decorator
def my_func():
    return "Hello"

print(my_func()) # Hello World
print(my_func)

def five_times_decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(5):
            func()
    return wrapper

@five_times_decorator
def print_test():
    print("test")

# Нужно написать декоратор, который умножает результат выполнения
# функции на 2


def multiply_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@multiply_decorator
def add(a, b):
    return a + b

print(add(1, 2))
