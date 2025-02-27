import tkinter as tk
from model import EmployeeModel
from view import EmployeeWindowedView
from controller import EmployeeController

if __name__ == "__main__":
    root = tk.Tk()
    model = EmployeeModel()
    controller = EmployeeController(model, None)
    view = EmployeeWindowedView(root, controller)
    controller.view = view
    model.add_observer(view)
    view.create_gui()
    root.mainloop()
