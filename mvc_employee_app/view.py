import tkinter as tk
from tkinter import messagebox


class EmployeeWindowedView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

    def create_gui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Имя:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Должность:").grid(row=1, column=0)
        self.position_entry = tk.Entry(self.frame)
        self.position_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Зарплата:").grid(row=2, column=0)
        self.salary_entry = tk.Entry(self.frame)
        self.salary_entry.grid(row=2, column=1)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        tk.Button(
            self.root,
            text="Удалить",
            command=self.controller.delete_employee
        ).pack(pady=5)
        tk.Button(
            self.frame,
            text="Добавить",
            command=self.controller.add_employee
        ).grid(row=3, columnspan=2, pady=5)
        tk.Button(
            self.frame,
            text="Обновить",
            command=self.controller.update_employee
        ).grid(row=4, columnspan=2, pady=5)

    def update(self, employees):
        self.listbox.delete(0, tk.END)
        for emp in employees:
            self.listbox.insert(
                tk.END,
                f"{emp['name']} - {emp['position']} - {emp['salary']}"
            )

    def get_employee_data(self):
        return self.name_entry.get(), self.position_entry.get(), self.salary_entry.get()

    def set_employee_data(self, name, position, salary):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)

        self.position_entry.delete(0, tk.END)
        self.position_entry.insert(0, position)

        self.salary_entry.delete(0, tk.END)
        self.salary_entry.insert(0, salary)

    def get_selected_index(self):
        selected = self.listbox.curselection()
        return selected[0] if selected else None

    def on_select(self, event):
        index = self.get_selected_index()
        if index is not None:
            self.controller.select_employee(index)

    def show_error(self, message):
        messagebox.showerror("Ошибка", message)
