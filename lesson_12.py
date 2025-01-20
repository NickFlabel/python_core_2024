# Объектно-ориентированное программирование (ООП)

# Объект в программировании это сущность, которая объединяет в себе
# как данные (переменные) и функции, работающие с этими данными

students = []

def add_student(name, age, grade):
    students.append({"name": name, "age": age, "grade": grade})

def print_studet(student):
    print(f"Имя: {student['name']}")

add_student("Студент 1", 20, 90)
add_student("Студент 2", 22, 85)

for student in students:
    print_studet(student)


# Абстракция
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Оценка: {self.grade}")

student1 = Student(name="Student 1", age=20, grade=90)
student2 = Student(name="Student 2", age=22, grade=85)
student1.print_info()
student2.print_info()

# class - это "чертеж" или "шаблон" для создания объектов

# Объект - это конкретный экземпляр класса (student1 и student2 -
# объекты или конкретные экземпляры класса Student)

# ВСЕ что у нас есть в Python - объект того или иного класса

# Методы - функции, опредленные внутри класса

# Аттрибуты - переменные, привязанные к объекту
# self.name, self.age ...


class Point:
    ...

p1 = Point()
p1.x = 10
p1.y = 20
print(p1)
print(p1.x)
print(p1.y)
p2 = Point()
print(p2)

class Student:
    ...

student1 = Student()
student2 = Student()
student1.name = "name 1"
student1.name = "new name"
student2.name = "name 2"
print(student1.name)

# Функция hasattr - возвращает True если у объекта есть нужный
# аттрибут и False - если нет
print(hasattr(student1, "name")) # Такой аттрибут есть -> True
print(hasattr(student1, "age")) # Такого аттрибута нет -> False
print(hasattr(student1, "__str__")) # __str__ - метод, который есть
# по умолчанию у любого объекта

# Методы объектов
# У любого объекта есть заранее определенный языком Python набор
# методов, которые играю особую роль
# такие методы называются dunder-методы или магические методы
# С точки зрения синтаксиса dunder-методы обособляются двумя
# нижними подчеркиваниями с обоих сторон


# __init__() - особый метод - конструктор, который вызывается сам
# при создании нового экземпляра класса
class Student:
    def __init__(self, name):
        print(f"Новый экземпляр класса Student был создан с именем {name}")

    def my_method(self, a, b):
        return a + b

student1 = Student("new name")
print(student1.my_method(1, 2))

# self - ссылка на экземпляр класса с которым мы работаем

class Teacher:
    def __init__(self, name, age):
        self.name = name # teacher.name = name
        self.age = age

    def print_info(self):
        print(f"Имя: {self.name}. Возраст: {self.age}")

teacher = Teacher(name="teacher 1", age=35)
print(teacher.name)
print(teacher.age)
teacher.print_info()

# Абстракция - мы берем какой-то реальный объект и описываем его
# в плане тех свойств реального объекта, которые нужны нашей логике
# приложения

# Инкапсуляция - мы определяем принадлежность аттрибутов и методов
# которые будут касаться только конкретного экземпляра объекта

class Animal:
    def __init__(self, species):
        self.species = species

    def __str__(self):
        return f"Животное вида {self.species}"

cat = Animal(species="cat")
print(cat) # функция print вызывает метод __str__() у объекта

class Point:
    x = 10
    y = 20

    def __add__(self, other): # От опредения метода __add__ зависит
# то, как объект будет вести себя при использовании оператора +
        result = Point()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __eq__(self, other): # Метод для выполнения оператора сравнения
        return self.x == other.x and self.y == other.y


p1 = Point()
p2 = Point()
p3 = p1 + p2
print(p3.x, p3.y)
print(p1 == p2)

# __add__ - +
# __eq__ - ==
# __sub__ - -
# __div__ - /
# __mul__ - *


# Задание №1
# Создайте класс Rectangle, который будет представлять прямоугольник.
# У каждого прямоугольника должны быть аттрибуты length (длина)
# и width (ширина)
# Добавьте метод area, который вычисляет площадь прямоугольника
# Создайте несколько объектов и вычислите их площади

# Задание 2
# Создайте класс Student, который будет представлять студента
# У каждого студента есть метод is_passed, который возвращает
# True, если оценка студента больше или равна 60 иначе False
# Создайте несколько студентов и проверьте, кто из них сдал экзамен
