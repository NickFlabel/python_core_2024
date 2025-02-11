# pip - это менеджер пакетов для python
# который позволяет устанавливать сторонние библиотеки
# из репозитория PyPI

# Чтобы удостовериться, что pip корректно устанвлен можно
# ввести команду pip --version

# Если pip отсутствует на компьютере или установлен некорректно,
# то мы можем использовать команду python -m ensurepip

# Для макбука - каждый раз когда я буду писать просто pip
# вы пишете python3 -m pip

# Библиотека colorama - делает вывод в консоль цветным

# Для уставки библеотеки введите в консоль
# pip install colorama

from colorama import Fore, Style

print(Fore.RED + "Этот текст красный" + Style.RESET_ALL)

# pyfiglet - библеотека с текстовыми ASCII-баннерами
# pip install pyfiglet

import pyfiglet
print(pyfiglet.figlet_format("Hello"))

# Для удаления пакетов используется команда pip uninstall
# Для обновления сторонней библиотеки используется команда
# pip install --upgrade

# pip freeze - важная команда, которая выводит установленные
# пакеты на экран

# pip freeze > requirements.txt - команда, сохраняющая все
# установленные пакеты в файл requirements.txt для последующего
# использования другими разработчиками или нами самими

# pip install -r requirements.txt - устанавливает все зависимости
# которые перечислены в файле requirements.txt

# На примере библиотеки requests посмотрим каким образом python
# может работать с http-запросами

# HTTP-протокол - это протокол для передачи данных в интернете
# HTTP-протокол строится по принципу клиент-серверной архитектуры

# По стандарту HTTP запрос должен обладать следующими характеристиками
# Запрос должен иметь метод
# GET - запрос, который просит сервер предоставить какую-то информацию
# POST - запрос с таким методом просит сервер добавить какую-то информацию
# PUT - запрос с таким методом просит сервер изменить существующие данные
# DELETE - запрос с таким методом просит сервер удалить данные

# Второй важный элемент - ресурс (url в адресной строке)

# HTTP-ответ
# Ключевой аспект ответа - статусный код

# 200 OK - запрос выполнен успешно
# 201 Created - Объект создан
# 204 No Content - Успешный запрос без данных (DELETE)
# 400 Bad Request - Ошибка в запросе
# 401 Unauthorize - требуется авторизация
# 403 Forbidden - доступ запрещен
# 404 Not Found - Ресурс не найден
# 500 Internal Server Error - Ошибка на сервере

# Для удобной работы с HTTP-запросами у нас есть библиотека requests
# pip install requests

import requests

# request = requests.get("https://example.com")
#
# print("Статус-код: ", request.status_code)
# with open("response.html", "w") as f:
#     f.write(str(request.content))

# Как работать с json
# https://api.sampleapis.com/coffee/hot

url = "https://api.sampleapis.com/coffee/hot"
response = requests.get(url)

if response.status_code == 200:
    data = response.json() # Метод .json() расшифровывает пришедший
    # нам json и позволяет работать с ним как с обычными словарями
    # в python
    print("Первый кофе: ", data[0]["title"])
    print("Количество напитков: ", len(data))


# Задание:
# 1 Отправить GET - запрос на
# https://api.sampleapis.com/codingresourses/codingResources
# 2. Получить и обработать данные
# 3. Сохранить их в файл coding_resources.json
# 4. есть аттрибут topics - отфильтровать только те записи, где
# в топиках есть html
