# У нас есть два момента, когда python обращается
# к файлу - начало работы и конец работы

employees = []
history = []
backup = []

def load_employees(file_name):
    global employees
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            employees.clear()
            for line in f:
                last_name, first_name, age, birthday = line.strip().split("|")
                employees.append({
                    "last_name": last_name,
                    "first_name": first_name,
                    "age": age,
                    "birthday": birthday,
                })
            print("Список сотрудников загружен")
    except FileNotFoundError:
        print("Файл не найден. Начием работу с пустого файла")


def save_employees(file_name):
    global employees
    with open(file_name, "w", encoding="utf-8") as f:
        for emp in employees:
            line = f"{emp['last_name']}|{emp['first_name']}|{emp['age']}|{emp['birthday']}"
            f.write(line)
    print("Список сотрудников сохранен")

def add_employee():
    global employees, history, backup
    backup = employees[:]
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    age = input("Введите возраст: ")
    birthday = input("Введите дату рождения: ")
    employees.append({
        "last_name": last_name,
        "first_name": first_name,
        "age": age,
        "birthday": birthday,
    })
    history.append(f"Добавлен сотрудник {first_name} {last_name}")

def edit_employee():
    global employees, backup # list[dict{}]
    backup = employees[:]
    last_name = input("Введите фамилию работника для поиска: ")
    for emp in employees:
        if emp["last_name"] == last_name:
            print(f"Найден сотрудник: {emp}")
            emp["last_name"] = input("Введите новую фамилию: ")
            emp["first_name"] = input("Введите новое имя: ")
            emp["age"] = input("Введите новый возраст: ")
            emp["birthday"] = input("Введите новый день рождения: ")
            history.append(f"Обновлен сотрудник {emp['first_name']} {emp['last_name']}")
            return
    print("Сотрудник с такой фамилией не найден")

def delete_employee():
    global employees, employees
    backup = employees[:]
    last_name = input("Введите фамилию работника для поиска: ")
    for i, emp in enumerate(employees): # вместо возвращения значения enumerate вернет индекс и значение
        if emp["last_name"] == last_name:
            del employees[i]
            history.append(f"Сотрудник {last_name} удален")
            return
    print("Сотрудник с такой фамилией не найден")

def undo_changes():
    global employees, backup
    employees = backup[:]

def main():
    file_name = input("Введите имя файла для загрузки сотрудников: ")
    # загружаем список сотрудников из файла
    load_employees(file_name)

    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Изменение информации о сотруднике")
        print("3. Удалить сотрудника")
        print("4. Показать историю")
        print("5. Отменить последнее изменение")
        print("0. Выход")

        choice = int(input("Ваш выбор: "))
        if choice == 1:
            # функция для добавления сотрудника
            add_employee()
        if choice == 2:
            # функция для редактирования сотрудника
            edit_employee()
        if choice == 3:
            # функция для удаления сотрудника
            delete_employee()
        if choice == 5:
            # функция для отката изменений
            undo_changes()
        if choice == 0:
            # функция для сохранения временных данных в файл
            save_employees(file_name)
            print("Программа завершена")
            break
        else:
            print("Неверный выбор")


if __name__ == '__main__':
    main()
