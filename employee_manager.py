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


##### Хранение данных

def load_data():
    """
    Читает данные из JSON-файла и загружает список сотрудников
    в виде поддерживаемых python типов данных
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file) # Преобразование JSON из файла в
        # тип данных, поддерживаемый python
    except FileNotFoundError:
        return []


def save_data(data):
    """
    Принимает в качестве аргумента list (data) и сохраняет его в виде
    json в соответствующий файл
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


##### GUI-часть

root = tk.Tk()
root.title("Управление сотрудниками")

frame = tk.Frame(root)

