import tkinter as tk
from tkinter import messagebox
import json


class EmployeeManager:
    DATA_FILE = "employees.json"

    def __init__(self):
        self.employees = self.load_data()

    def load_data(self):
        try:
            with open(self.DATA_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data):
        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)


class EmployeeApp:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root

    def create_gui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Имя:").grid(row=0, column=0)
        name_entry = tk.Entry(self.frame)
        name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Должность:").grid(row=1, column=0)
        position_entry = tk.Entry(self.frame)
        position_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Зарплата:").grid(row=2, column=0)
        salary_entry = tk.Entry(self.frame)
        salary_entry.grid(row=2, column=1)

        tk.Button(
            self.frame,
            text="Добавить",
            command=self.add_employee
        ).grid(row=3, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack()

        self.update_listbox()

        tk.Button(
            self.root,
            text="Удалить",
            command=self.delete_employee
        ).pack(pady=5)

        self.listbox.bind("<<ListboxSelect>>", self.select_employee)

        tk.Button(
            self.frame,
            text="Обновить",
            command=self.update_employee
        ).grid(row=4, columnspan=2, pady=5)

    def add_employee(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        if not name or not position or not salary:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return

        try:
            salary = float(salary)
        except ValueError:
            messagebox.showerror("Ошибка", "Зарплата должна быть числом!")
            return

        new_employee = {"name": name, "position": position, "salary": salary}
        employees = self.manager.load_data()
        employees.append(new_employee)
        self.manager.save_data(employees)

        # Обновление списка работников
        self.update_listbox()

        # Удаляем уже ненужные введенные данные
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

    def update_listbox(self):
        # Загружаем список работников из БД
        employees = self.manager.load_data()
        # Очищаем текущий список работников
        self.listbox.delete(0, tk.END)
        # Заполняем список
        for emp in employees:
            self.listbox.insert(
                tk.END,
                f"{emp['name']} - {emp['position']} - {emp['salary']}"
            )

    def delete_employee(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Ошибка", "Выберите сотрудника для удаления")
        employees = self.manager.load_data()
        index = selected[0]
        del employees[index]
        self.manager.save_data(employees)
        self.update_listbox()

    def select_employee(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return
        employees = self.manager.load_data()
        index = selected[0]
        emp = employees[index]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, emp["name"])

        self.position_entry.delete(0, tk.END)
        self.position_entry.insert(0, emp["position"])

        self.salary_entry.delete(0, tk.END)
        self.salary_entry.insert(0, emp["salary"])

    def update_employee(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Ошибка", "Выберите сотрудника для обновления")
            return

        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        if not name or not position or not salary:
            messagebox.showerror("Ошибка", "Заполните все поля")
            return

        try:
            salary = float(salary)
        except ValueError:
            messagebox.showerror("Ошибка", "Зарплата должна быть числом")
            return

        employees = self.manager.load_data()
        index = selected[0]
        employees[index] = {"name": name, "position": position, "salary": salary}
        self.manager.save_data(employees)
        self.update_listbox()


if __name__ == "__main__":
    manager = EmployeeManager()
    root = tk.Tk()
    app = EmployeeApp(root, manager)
    app.create_gui()
    root.mainloop()


