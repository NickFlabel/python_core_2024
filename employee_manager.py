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
from tkinter import messagebox
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
frame.pack(pady=10) # pady - расстояние от верха окна в пикселях

# Поля для ввода информации
tk.Label(frame, text="Имя:").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Должность:").grid(row=1, column=0)
position_entry = tk.Entry(frame)
position_entry.grid(row=1, column=1)

tk.Label(frame, text="Зарплата:").grid(row=2, column=0)
salary_entry = tk.Entry(frame)
salary_entry.grid(row=2, column=1)

def add_employee():
    name = name_entry.get() # метод get() возвращает то, что пользователь
    # ввел в соответствующее поле
    position = position_entry.get()
    salary = salary_entry.get()

    if not name or not position or not salary:
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return
        # Открывает новое окно с ошибкой

    try:
        salary = float(salary)
    except ValueError:
        messagebox.showerror("Ошибка", "Зарплата должна быть числом!")
        return

    new_employee = {"name": name, "position": position, "salary": salary}
    employees = load_data()
    employees.append(new_employee)
    save_data(employees)

    # Удаляем уже ненужные введенные данные
    name_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

tk.Button(
    frame,
    text="Добавить",
    command=add_employee
).grid(row=3, columnspan=2, pady=5) # columnspan - сколько колонок занимает
# элемент

root.mainloop()

