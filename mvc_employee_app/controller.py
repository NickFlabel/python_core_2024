class EmployeeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_employee(self):
        name, position, salary = self.view.get_employee_data()

        if not name or not position or not salary:
            self.view.show_error("Заполните все поля!")
            return

        try:
            salary = float(salary)
        except ValueError:
            self.view.show_error("Зарплата должна быть числом!")
            return

        self.model.add_employee(name, position, salary)

    def select_employee(self, index):
        if 0 <= index <= len(self.model.employees):
            emp = self.model.employees[index]
            self.view.set_employee_data(
                emp["name"],
                emp["position"],
                emp["salary"]
            )

    def update_employee(self, index=None):
        if index is None:
            selected = self.view.get_selected_index()
            if selected is None:
                self.view.show_error("Выберете сотрудника для обновления!")
            index = selected

        name, position, salary = self.view.get_employee_data()

        if not name or not position or not salary:
            self.view.show_error("Заполните все поля!")
            return

        try:
            salary = float(salary)
        except ValueError:
            self.view.show_error("Зарплата должна быть числом!")
            return

        self.model.update_employee(index, name, position, salary)

    def delete_employee(self, index=None):
        if index is None:
            selected = self.view.get_selected_index()
            if selected is None:
                self.view.show_error("Выберете сотрудника для обновления!")
            index = selected

        self.model.delete_employee(index)
