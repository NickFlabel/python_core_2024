# Необходимо реализовать систему управления персоналом
# с исполтьзованием GUI на основе tkinter

# CRUD с сущностью "работник"
# С - create
# R - retrieve
# U - update
# D - delete

# Хранение данных - json-файл

# 1) Хранение данных
# 2) Создает графический интерфейс для пользователя для взаимодействия с данными


import tkinter as tk
import json

# Имя файла для хранения данных
DATA_FILE = "employees.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file) # Преобразование JSON из файла в
        # тип данных, поддерживаемый python
    except FileNotFoundError:
        return []


