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

def main():
    file_name = input("Введите имя файла для загрузки сотрудников: ")
    # загружаем список сотрудников из файла

    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Изменение информации о сотруднике")
        print("3. Удалить сотрудника")
        print("4. Найти сотрудника")
        print("0. Выход")

        choice = int(input("Ваш выбор: "))
        if choice == 1:
            # функция для добавления сотрудника
            ...
        if choice == 2:
            # функция для редактирования сотрудника
            ...
        if choice == 3:
            # функция для удаления сотрудника
            ...
        if choice == 0:
            # функция для сохранения временных данных в файл
            print("Программа завершена")
            break
        else:
            print("Неверный выбор")


if __name__ == '__main__':
    main()
