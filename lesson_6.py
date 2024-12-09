# Исключения - это событие, которое возникает во время выполнения
# программы и нарушает ее нормальный поток выполнения

# list с длинной 2, а мы пытаемся обратится к индеку 10 ->
# IndexError
# "a" + 5 -> TypeError
# 1 / 0 -> DivisionByZero

# IndentationError: - ошибка, связанная с отсутствием
# необходимых отступов
# if True:
# print("exception")

# ValueError - возникает, когда передано значение неверного типа
# int("hello") # -> ValueError

# TypeError - при использовании операторов с неверными типами
# "string" + 5

# IndexError - когда запрошенный индекс выходит за пределы последовательности
# lst = [1, 2]
# print(lst[10])

# AttributeError - когда у сущности нет какого-либо аттрибута
# lst = [1, 2]
# lst.append(3) # у объекта типа list есть метод append
# st = "my_str"
# st.append("2")

# MemoryError - возникает, когда программа не может выделить
# необходимую ей память для операции
# big_list = [0] * (10**10)

import random


# Для того чтобы обработать какое-либо исключение
# у нас есть сочетание слов try/except
# они нужны для того чтобы не прерывать работу программы
# в случае возникновения ошибки
#
# try:
#     a = 10 / 0
# except:
#     print("Возникла ошибка!")

# try-блок содержит в себе код, который потенциально может
# вызвать исключение
# except-блок содержит в себе код, который выполняется после
# того как исключение было вызвано

# "голый" except-блок ловит все исключения, которые есть
# в python
# Для того чтобы конкретизировать, какие ошибки мы хотим
# словить мы должны прописать конкретный класс ошибок после
# слова except
#
# try:
#     10 / 0
# except ZeroDivisionError: # данный блок работает только с ValueError
#     print("возникла ошибка ValueError")
#
#
# try:
#     lst = []
#     print(lst[1])
# except (IndexError, ValueError): # Мы можем ловить сразу несколько типов ошибок
#     print("Возникла IndexError или ValueError")
#

def get_currency_rates():
    is_query_successfull = random.choice([True, False])
    if is_query_successfull:
        return [11, 22, 33]
    else:
        # Мы можем сами в Python вызывать исключения
        raise TimeoutError

import time

def currency_exchange_agency():
    while True:
        try:
            exchange_rates = get_currency_rates()
            print(f"Dollar - {exchange_rates[0]}")
        except TimeoutError:
            print("Возникла ошибка - нет ответа от сервера")
        time.sleep(1)

# currency_exchange_agency()

# кроме try/except у нас также есть еще ключевое слово
# finally, которая используется в этой же связке

# Блок finally используется тогда, когда у нас есть необходимость
# исполнить какой-либо код как в случае, когда все пошло хорошо,
# так и в случае, когда наша программа вызвала исключение

# try: # код, который исполняется только если он не вызывает ошибок
#     10 / 0
# except ZeroDivisionError: # код, который выполняется только если
#     # произошла ошибка
#     print("Деление на ноль")
# finally: # код который выполняется в любом из случаев
#     print("Код, который выполняется всегда")


def connect_to_database():
    print("Соединение с БД установлено")

def close_connection():
    print("Соединение с базой данных установлено")

def query_by_pk(pk):
    if pk < 10:
        return "Объект"
    else:
        raise ValueError

def get_item_by_pk_and_establish_connection(pk):
    connect_to_database()
    try:
        query_by_pk(pk)
    except ValueError:
        print("Возникла ошибка при попытке запроса в БД")
    finally:
        close_connection()

# get_item_by_pk_and_establish_connection(100)

user_input = input()
try:
    user_input = int(user_input)
except ValueError as e: # as == (=) или e = ValueError()
    print(e)
    print("Неверное значение")
@FlaviusBelisarius