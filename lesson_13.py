# Абстракция - выделие ключевых характеристик объекта,
# скрывая детали реализации
list = []
# Упрощает использование сложных систем
# Скрывает ненужные детали от пользователя, предоставляя ему
# только необходимую информацию
# Создает четкие интерфейсы для взаимодействия с объектами

list.append(1)
# Интерфейс - все публичные способы взаимодействия с
# каким-либо объектом

class Car:
    def start(self):
        print("Автомобиль завелся")

    def stop(self):
        print("Автомобиль остановился")

car = Car()
car.stop()

# Инкапсуляция - ограничение доступа к внутренним данным и методам
# объекта, предоставляя только те части, которые нужны пользователю

# Инкапсуляция улучшает безопасность данных
# Уменьшает риск некорректного использования объекта
# Делает объект более понятным, скрывая лишние детали

# Уровни доступа
# Публичные или открытые аттрибуты и методы

class Cat:
    color = "white" # Публичный аттрибут - я могу получить доступ
    # через .color

    def meow(self): # Публичный метод
        print("meow")

# Защищенные или protected аттрибуты и методы
# Среди разработчиков существует договоренность, что
# аттрибуты и методы название которых начинается с одного
# нижнего подчеркивания нельзя использовать вне самого класса

class Cat:
    _color = "white"

    def get_color(self):
        return self._color

cat = Cat()
print(cat._color) # Этот код сработает, но с точки зрения стандартов
# Это не верно

class Counter:
    _counter = 0

    def get_counter(self):
        self._counter += 1
        return self._counter

# Приватные (Private) аттрибуты и методы
# Приватные аттрибуты и методы обособляются двумя
# нижними подчеркиваниями

class Dog:
    __sound = "bark"

    def bark(self):
        return self.__sound # name dagling - коверканье имени
    # когда python видит внутри класса название __<attr name>
    # он превращает его в _<class name>__<attr name>

dog = Dog()
print(dog._Dog__sound)

class Search:
    def __init__(self, lst):
        self.lst = lst

    def search(self, value):
        return self.__search_algorythm(self.lst, value)

    def __search_algorythm(self, lst, value):
        for i in range(len(lst)):
            if lst[i] == value:
                return i

# методы-геттеры и методы-сеттеры

class Student:
    _name = "name"
    _age = 10

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

student = Student()
print(student._name)

# Наследование - механизм объектно-ориентированного программирования,
# который позволяет одному классу (называемому дочерним) унаследовать
# аттрибуты и методы другого класса (называемого родительским).

class Animal:
    sound = "undefined"

    def make_sound(self):
        return self.sound

class Cat(Animal): # Класс Cat наследуется от класса Animal и
    # получает от него все аттрибуты и методы, определенные в
    # родительском классе
    sound = "meow"

class Bird(Animal):
    def fly(self): # Мы можем добавлять методы и аттрибуты, которых
        # в родительском классе нет
        print("This bird flies")

class Fish(Animal):
    def make_sound(self): # Мы можем переопределять существующие
        # методы и аттрибуты, доставшиеся нам от родительского класса
        print("No sound")

cat = Cat()
print(cat.make_sound()) # фактически - make_sound(cat)
bird = Bird()
print(bird.make_sound())
fish = Fish()
fish.make_sound()

# Преимущества наследования
# Отсутствие дублирования кода
# Облечает расширение функциональности
# Позволяет создавать иерархии классов

# Полиморфизм
# Способность объектов разного типа использовать один и тот же
# интерфейс. Это означает, что один и тот же метод или операция
# может вести себя по-разному в зависимости от объекта, который
# его использует

# Повышает гибкость кода
# Пример - базовый класс кассовый аппарат и два подкласса
# Уменьшает дублирование кода
# Упрощает расширяемость классов

# Использование аттрибутов и методов родительского класса
class Bike:
    def __init__(self, make):
        self.make = make

class Motobike(Bike):
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine

# В python есть специальная функция super(), которая позволяет
# получать доступ к аттрибутам и методам родительского
# класса как они определены в нем

class Bike:
    def __init__(self, make):
        self.make = make


class Motobike(Bike):
    def __init__(self, *args, engine, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine

class Controller:
    def execute(self):
        return "Веб-страница"

class LoginRequiredMixin:
    def check_premissions(self):
        return True

class MainPageController(Controller, LoginRequiredMixin):
    ...


class A:
    def my_method(self):
        print("A")

class B:
    def my_method(self):
        print("B")

class C(A, B):
    ...

c = C()
c.my_method()


class TransportVehicle:
    _vehicle_type = "Неопределенное транспортное средство"

    def __init__(self, make, speed):
        self.make = make
        self.speed = speed

    def description(self):
        print(f"{self._vehicle_type} Марка: {self.make} - скорость: {self.speed}")

class Car(TransportVehicle):
    _vehicle_type = "Автомобиль"

class Bicycle(TransportVehicle):
    _vehicle_type = "Велосипед"

bicycle = Bicycle("марка", 15)
car = Car("volvo", 100)

car.description()
bicycle.description()
