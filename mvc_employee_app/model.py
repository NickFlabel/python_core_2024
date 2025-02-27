import json


class EmployeeModel:
    DATA_FILE = "employees.json"

    def __init__(self):
        self.employees = self.load_data()
        self.observers = []

    def load_data(self):
        try:
            with open(self.DATA_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.DATA_FILE, "w") as file:
            json.dump(self.employees, file, indent=4)
        self.notify_observers()

    def add_employee(self, name, position, salary):
        self.employees.append(
            {"name": name, "position": position, "salary": salary}
        )
        self.save_data()

    def update_employee(self, index, name, position, salary):
        self.employees[index] = {
            "name": name,
            "position": position,
            "salary": salary
        }
        self.save_data()

    def delete_employee(self, index):
        del self.employees[index]
        self.save_data()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.employees)
