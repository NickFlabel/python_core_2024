# Label (Метка)

from tkinter import Tk, Label

# root_label = Tk()
# root_label.title("Окно с Label")
#
# label = Label(
#     root_label, # Связываем виджет с основным процессом
#     text="Приложение с Label", # Текст, отображаемый в окне
#     font=("Arial", 24), # Шрифт (<имя шрифта>, <размер шрифта>)
#     bg="lightblue", # (r, g, b) название или цифровые параметры цвета
#     fg="darkblue",
# )
# label.grid(column=0, row=0)

# Button (кнопка)
from tkinter import Button

# root_button = Tk()
# root_button.title("Окно с Button")

# def on_click():
#     print("Кнопка была нажата")
#
# button = Button(
#     root_button,
#     text="Кнопка",
#     bg="green",
#     fg="white",
#     command=on_click, # В command передается вызываемый объект
#     # (как правило функция), который будет выполняться при нажатии
#     # кнопки
# )
# button.grid(column=0, row=0)
#
# root_button.mainloop()


# Entry (Однострочное текстовое поле)

from tkinter import Entry

# entry_root = Tk()
# entry_root.title("Окно с Entry")
#
# entry = Entry(
#     entry_root,
#     show="*", # Сокрытие введенного текста за *
#     width=30, # ширина нашего поля или сколько символов оно вмещает
# )
# entry.pack(
#     padx=10, # Отступ в пикселях по оси x
#     pady=10,
# )
#
# def show_text():
#     print(entry.get()) # Метод get(), примененный на Entry возвращает
#     # введеннй в Entry текст в виде str
#
# button = Button(
#     entry_root,
#     text="Показать введенный текст",
#     command=show_text,
# )
# button.pack(pady=10)
#
# entry_root.mainloop()


# Text - Многострочное текстовое поле
from tkinter import Text

# text_root = Tk()
# text_root.title("Окно с Текстом")
#
# text = Text(
#     text_root,
#     width=30,
#     height=5,
#     wrap="word",
# )
# text.pack(
#     pady=10,
#     padx=10
# )
#
# text_root.mainloop()

# Checkbutton (Флаг)

from tkinter import Checkbutton, IntVar

# checkbutton_root = Tk()
# checkbutton_root.title("Окно с флагом")
#
# var = IntVar()
#
# check = Checkbutton(
#     checkbutton_root,
#     text="Я согласен",
#     variable=var,
# )
# check.pack(pady=10)
#
# checkbutton_root.mainloop()
# print(var.get())


# Radiobutton (Переключатель)
from tkinter import Radiobutton, StringVar

# radio_root = Tk()
# radio_root.title("Окно с переключателем")
#
# var = StringVar(value="option_1")
#
# button1 = Radiobutton(
#     radio_root,
#     text="Option 1",
#     value="option_1",
#     variable=var,
# )
# button1.pack()
# button2 = Radiobutton(
#     radio_root,
#     text="Option 2",
#     value="option_2",
#     variable=var,
# )
# button2.pack()
#
# radio_root.mainloop()
# print(var.get())


# JSON и работа с ним
# JSON - JavaScript Object Notation - аналог словарей в язке
# JavaScript

# Работа с JSON у нас происходит при помощи встроенной библиотеки
# json

import json
# Преобразование python в JSON
data = {
    "login": "nickname",
    "password": "password",
}

json_str = json.dumps(data, indent=4)
# dumps() - преобразование в json-строку
# print(data)

# dump() - сохранение json в файл
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json") as f:
    data = json.load(f)

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система управления персоналом")
        self.root.geometry("500x400")

        self.data_file = "employees.json"

        self.employees = []

        self.load_data()
        self.create_widgets()

    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                self.employees = json.load(f)
        except FileNotFoundError:
            with open(self.data_file, "w"):
                ...

    def create_widgets(self):
        # Поле для заполнения имени
        self.label_name = Label(self.root, text="Имя:")
        self.label_name.grid(row=0, column=0, pady=10, padx=10)
        self.entry_name = Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        # Кнопка для сохранения работника
        self.button_add = Button(
            self.root,
            text="Добавить работника",
            command=self.add_employee,
        )
        self.button_add.grid(row=1, column=1, pady=10, padx=10)
        self.employee_labels = []
        for i, employee in enumerate(self.employees):
            employee_label = Label(
                self.root,
                text=f"{i}) Имя: {employee['name']}"
            )
            employee_label.grid(row=2+i, column=1)
            self.employee_labels.append(employee_label)

    def add_employee(self):
        name = self.entry_name.get()
        if not name:
            return
        self.employees.append({"name": name})

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.employees, f, indent=4)

root = Tk()
app = EmployeeManagementApp(root)
root.mainloop()
app.save_data()
