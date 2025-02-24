def decorator(func):
    def wrapper(*args, **kwargs):
        # код до выполнения основной функции
        print(func)
        result = func(*args, **kwargs)
        print("Промежуточный результат: ", result)
        # Делаю что-то с результатом выполнения функции
        return result * 2
    return wrapper

@decorator
def my_func(a, b):
    return a + b

# decorated_function = decorator(my_func) # тоже самое что
# # @decorator над функцией
#
# print(decorated_function(2, 1))
#
#
# def apply_function_to_list(func, lst):
#     """
#     Эта функция обрабатывает список, состоящий из двух значений, применяя
#     к ним функцию func
#     """
#     for elem in lst:
#         print(func(*elem))
#
# lst = [(1, 2), (2, 3)]
# apply_function_to_list(my_func, lst)


def print_decorator(func):
    def wrapper():
        print("До функции")
        func() # подставляет функцию, которую мы передали в качестве аргумента
        # на это место
        print("После функции")
    return wrapper

@print_decorator # тоже самое что print_decorator(my_func_2)
def my_func_2():
    print("Функция my_func_2")

# decorated_function = print_decorator(my_func_2)
# # в decorated_function у нас по сути хранится wrapper с подставленной
# # вместо func() нашей функцией my_func_2
# decorated_function()

print(my_func_2)
my_func_2()

# Декоратор как паттерн проектирования

# Сеть кофеен - у нас есть меню, которое необдимо реализовать
# в виде классов

from abc import abstractmethod

class Beverage:
    @abstractmethod
    def get_description(self):
        ...

    @abstractmethod
    def cost(self):
        ...

class Espresso(Beverage):
    def get_description(self):
        return "Эспрессо"

    def cost(self):
        return 1000


class Tea(Beverage):
    def get_description(self):
        return "Чай"

    def cost(self):
        return 500


class AdditionDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        ...


class Milk(AdditionDecorator):
    def cost(self):
        return self.beverage.cost() + 100

    def get_description(self):
        return self.beverage.get_description() + ", молоко"


class Sugar(AdditionDecorator):
    def cost(self):
        return self.beverage.cost() + 50

    def get_description(self):
        return self.beverage.get_description() + ", сахар"

class Lemon(AdditionDecorator):
    def cost(self):
        return self.beverage.cost() + 50

    def get_description(self):
        return self.beverage.get_description() + ", лимон"

tea = Tea()
prepared_tea = Sugar(tea)
prepared_tea = Milk(prepared_tea)
prepared_tea = Milk(prepared_tea)
prepared_tea = Lemon(prepared_tea)
print(prepared_tea.cost(), prepared_tea.get_description())

# декоратор - паттерн проектирования, который позволяет нам изменять
# поведение других объектов, не меняя при этом их реализацию

# Наблюдатель

# Этот паттерн позволяет оповещать объекты о событиях, которые могут их
# заинтересовать

# Метеостанция - устройство, которое собирает данные
# WeatherData - объект, которые получает данные от метеостанции и
# хранит их
# Экраны - классы, отображающие текущие погодные данные
#
# class WeatherData:
#     def __init__(self, display):
#         self.temperature = 0
#         self.pressure = 0
#         self.display = display
#
#     def get_temperature(self):
#         return self.temperature
#
#     def get_pressure(self):
#         return self.pressure
#
#     def update(self, temperature, pressure):
#         self.temperature = temperature
#         self.pressure = pressure
#         self.display.update(temperature, pressure)
#
#
# class CurrentConditionsDisplay:
#     def update(self, temperature, pressure):
#         print(f"Текущие погодные условия. Температура: {temperature}, давление: {pressure}")
#
#
# class ConditionsDisplay:
#     def update(self, temperature, pressure):
#         print(f"Текущие погодные условия. Температура: {temperature}, давление: {pressure}")
#
#
# display = CurrentConditionsDisplay()
# weather_data = WeatherData(display)
# weather_data.update(-10, 1000)


class Observer: # Интерфейс объекта, который наблюдает за изменениями
    # в других объектах
    @abstractmethod
    def update(self):
        ...

class Subject: # объект, за которым наблюдают Observer'ы
    @abstractmethod
    def register(self, observer: Observer):
        """
        Метод, позволяющий нам зарегестрировать наблюдателя
        за объектом
        """
        ...

    @abstractmethod
    def remove_observer(self, observer: Observer):
        """
        Метод, позволяющий убрать наблюдателя из списка наблюдателей
        """
        ...

    @abstractmethod
    def notify_observers(self):
        """
        Метод, позволяющий уведомить всех наблюдателей о произошедшем
        событии
        """

class WeatherData(Subject):
    def __init__(self):
        self.temperature = 0
        self.pressure = 0
        self.observers = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.pressure)

    def update_data(self, temperature, pressure):
        self.temperature = temperature
        self.pressure = pressure
        self.notify_observers()

class CurrentConditionsDisplay(Observer):
    def update(self, temperature, pressure):
        print(f"Текущие погодные условия. Температура: {temperature}, давление: {pressure}")


class VerboseTemperatureDisplay(Observer):
    def update(self, temperature, pressure):
        print("Холодно" if temperature < -20 else "Тепло")

weather_station = WeatherData()
weather_station.update_data(-21, 1000) # еще нет ни одного наблюдателя
display1 = CurrentConditionsDisplay()
weather_station.register(display1) # Зарегестрировали первого наблюдателя
weather_station.update_data(-25, 1000) # Первый наблюдатель отреагировал
display2 = VerboseTemperatureDisplay()
weather_station.register(display2)
weather_station.update_data(-15, 1000)
weather_station.remove_observer(display1)
weather_station.update_data(-30, 1000)

