# pip install flask
from flask import Flask, render_template, url_for, redirect, request
from controller import EmployeeController
from model import EmployeeModel

app = Flask(__name__)

model = EmployeeModel()
controller = EmployeeController(model=model, view=None)

@app.route("/employees")
def index():
    employees = model.employees
    return render_template("index.html", employees=employees)


@app.route("/add", methods=["POST"])
def add_employee():
    # когда мы обрабатываем запрос в flask нам приходит
    # объект класса request
    name = request.form.get("name")
    position = request.form.get("position")
    salary = request.form.get("salary")
    controller.add_employee(name, position, salary)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()


