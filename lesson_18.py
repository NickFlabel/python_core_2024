# # https://restful-api.dev/
#
# import requests
# import json
#
# url = "https://api.restful-api.dev/objects"
#
# # request = requests.get(url)
# #
# # print(request.status_code)
# # print(request.json())
#
# data = {
#    "name": "Apple MacBook Pro 25",
#    "data": {
#       "year": 2026,
#       "price": 2000.99,
#       "CPU model": "Intel Core i999",
#       "Hard disk size": "20 TB"
#    }
# }
#
# data = json.dumps(data)
# headers = {"content-type": "application/json"}
# response = requests.post(url, data=data, headers=headers)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Ошибка: ", response.status_code)
#
# updated_data = {
#    "name": "Apple MacBook Pro 2500",
#    "data": {
#       "year": 2026,
#       "price": 2000.99,
#       "CPU model": "Intel Core i999",
#       "Hard disk size": "20 TB"
#    }
# }
#
# updated_data = json.dumps(updated_data)
# headers = {"content-type": "application/json"}
# response = requests.put(
#     url + '/' + 'ff808181932badb60194f5adb4cb0691',
#     data=updated_data,
#     headers=headers
# )
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Ошибка: ", response.status_code)
#
#
# # FastAPI - один из самых популярных фреймворков для
# # создания своего API
# # pip install fastapi
# # pip install uvicorn - сервер
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/main_page/")
# def main():
#     return {"message": "hello world"}


# Многопроцессорность, многопоточность и асинхронность в Python
# Процесс - приложение, которое выполняется в процессоре
# Поток - часть процесса, которая выполняется вместе с другими потоками
# Асинхронность - параллельное, а не последовательное выполнение
# кода

# import multiprocessing
# import time
#
# def sum_numbers(n):
#     print("Функция начала выполнение")
#     total = sum(range(1, n))
#     time.sleep(2)
#     print(f"Функция завершила работу, результат = {total}")
#
# if __name__ == "__main__":
#     start = time.time()
#     process1 = multiprocessing.Process(target=sum_numbers, args=(5,))
#     process2 = multiprocessing.Process(target=sum_numbers, args=(5,))
#     process1.start()
#     process2.start()
#     process1.join()
#     process2.join()
#     print(f"Функции выполнились за {time.time() - start}")

# Создание процесса - дорогая с точки зрения компьютера
# операция. Используйте многопроцессорность только когда
# вы уверены, что она необходима для достижения
# результата


# Многопоточность
# Поток - часть процесса, которая может выполняться параллельно
# с другими потоками
# У потоков есть несколько преимуществ над процессом
# 1) Поток стоит меньше с точки зрения ресурсов компьютера
# 2) Доступ к общей памяти процесса

# import threading
# import time
# import requests
#
#
# def fetch_page(url):
#     print("Делаю запрос")
#     response = requests.get(url)
#     print("Завершаю запрос")
#
# def cpu_task():
#     total = 0
#     for i in range(10**7):
#         total += i
#
# if __name__ == "__main__": # 5.6 секунд - последовательные запросы
#     start = time.time()
#     cpu_task()
#     tasks = []
#     for i in range(3):
#         tasks.append(
#             threading.Thread(
#                 target=cpu_task
#             )
#         )
#     for task in tasks: # Запускаем потоки (без start() они ничего не
#         # будут делать
#         task.start()
#     for task in tasks: # Дожидаемся выполнения потоков (иначе наша
#         # программа продолжит работать хотя потоки не закончили работу)
#         task.join()
#     end = time.time()
#     print(f"Вычисления за {end - start} секунд")


# GIL - Global Interpreter Lock
# CPU-bound - задачи, которые нагружают процессор
# I/O-bound - задачи, которые зависят от третьих источников (диск, сервер)

# Асинхронность в Python
# Асинхронность в Python по своей сути - заполнение времени,
# которое python ничего бы не делал в ожидании результата
# другой задачи полезными действиями

# Асинхронный Python выполняется в рамках одного процесса и одного
# потока

# Центральное понятие асинхронности - цикл событий

# import asyncio
# import time
#
# async def hello():
#     print("Привет")
#     await asyncio.sleep(1)
#     print("Прошла одна секунда")
#
# async def cpu_task():
#     total = 0
#     for i in range(10**7):
#         total += i
#
# async def main():
#     start = time.time()
#     # task1 = asyncio.create_task(hello()) # добавил в список задач
#     # # функцию hello, но еще не начал ее исполнение
#     # task2 = asyncio.create_task(hello())
#     # # Добавил вторую задачу
#     # await task1 # Python увидел слово await и он отправился
#     # # выполнять первую задачу из списка
#     # await task2
#     tasks = []
#     for i in range(3):
#         tasks.append(asyncio.create_task(cpu_task()))
#     await asyncio.gather(*tasks)
#     end = time.time()
#     print(f"Прошло {end - start} секунд")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
# import asyncio
# import time
#
# import aiohttp
# import requests
# # pip install aiohttp
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.json()
#
# async def main():
#     start = time.time()
#     tasks = []
#     async with aiohttp.ClientSession() as session:
#         await fetch(session, "https://api.sampleapis.com/coffee/hot")
#     end = time.time()
#     print(f"100 запросов заняло {end - start} секунд")
#
# if __name__ == "__main__":
#     asyncio.run(main())


# Аннотация типов

a: int # Это указание для программиста и IDE что в этой переменной
# будет храниться int

# В первую очередь она используется в функциях

# import requests
# def add(a: int, b: int) -> str:
#     return a + b # IDE будет подсвечивать потому что мы написали,
# # что в результате функции выходит str
#
# result = "1" + add(1, 2)
#
# class MyClass:
#     arg1: int
#     client: requests
#
#     def __init__(self, client):
#         self.client = client
#
#     def fetch(self):
#         self.client.get()
#
# instance = MyClass(requests)

# pip install pydantic

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

user = User(id=1, name="3123", age=20)

my_data = [{"id": 1, "name": "name1", "age": 21},
           {"id": 2, "name": "name2", "age": 22}]

users = []
for user in my_data:
    users.append(User(**user))
print(users)
