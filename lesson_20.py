# Принципы SOLID
# Это хорошие практики для написания ООП-кода, сформулированные
# программистом Робертом Мартином (uncle Bob) в начале 2000-х годов

# S - Single Responsibility Principle (Принцип единственной ответственности)
# O - Open/Close Principle (Принцип открытости/закрытости)
# L - Barbara Liskov's Substitution Principle (Принцип подстановки
# Барбары Лисков
# I - Interface Segregation Principle (Принцип разделения интерфейсов)
# D - Dependency Inversion Principle (Принцип обратной зависимости)

# Принцип единственной ответственности простыми словами гласит, что
# у класса должна быть одна и только одна функция

class InfoProcessor:

    def get_info(self):
        # Получает информацию из интернета и сохраняет ее
        self.info = 'info'

    def print_infor(self):
        # выводит информацию на экран
        print(self.info)

# Формальное определение - класс должен иметь только одну причину
# для изменения

# Принцип открытости/закрытости
# Классы должны быть открыты для расширения и закрыты для модификации

class A:
    def __init__(self, arg):
        self.arg = arg

class B(A):
    def __init__(self, arg, arg2): # Неверно согласно принципу - я модифицировал
        # существующую логику
        self.arg = arg
        self.arg2 = arg2

class C(A):
    def __init__(self, arg, arg2): # Верно
        super().__init__(arg)
        self.arg2 = arg2

# Принцип подстановки Барбары Лисков
# Мы должны иметь возможность подставлять дочерние классы
# в любое место, которое могло принять родительский класс

# class A:
#     def execute(self, a):
#         print(a)
#
# class B(A):
#     def execute(self, a, b):
#         print(a, b)

class Money:
    def pay(self, amount):
        print(f"Осуществлен платеж на сумму {amount}")


class PaperMoney(Money): ...


class BankCard(Money):
    def pay(self, amount, card_number):
        print(f"Осуществлен платеж на сумму {amount} c карты {card_number}")


def payment_processor(money):
    money.pay(100)

abstract_money = Money()
payment_processor(money=abstract_money)
paper_money = PaperMoney()
payment_processor(paper_money)
# card_money = BankCard()
# payment_processor(card_money)

# Принцип разделения интерфейсов
# Клиент должен иметь доступ не к одному универсальному интерфейсу,
# а только к тем, которые ему нужны

class PaymentProcess:
    def process(self):
        # Принять платеж
        print("Сохранил в базу данных данные о платеже")
        # Отправить уведомление менеджеру
        print("Уведомление менеджеру отправлено")
        # занести платеж в список операций
        print("Платеж занесен в список операций")


# Принцип обратной зависимости

# Абстрактные классы и методы

# Абстрактный класс - это класс, который не может быть инстанциирован
# Абстрактные классы могут содержать как конкретные методы с реализацией
# так и абстрактные методы, которые ДОЛЖНЫ быть переобределены в
# дочерних классах

from abc import ABC, abstractmethod

class AbstractPaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        ...

class KaspiPaymentProcessor(AbstractPaymentProcessor):
    def pay(self):
        print("Оплата проведена при помощи Kaspi")

class PayPalPaymentProcessor(AbstractPaymentProcessor):
    def pay(self):
        print("Оплата проведена при помощи PayPal")

a = KaspiPaymentProcessor()
b = PayPalPaymentProcessor()
if isinstance(a, KaspiPaymentProcessor):
    a.pay()
else:
    a.pay_with_pay_pal()



# Принцип инверсии зависимостей гласит, что нам надо зависить не от
# конкретной реализации какого-либо класса, а от абстракции

# Простыми словами - мы не должны строить зависимости нашей программы
# от конкретных реализаций каждого класса вместо этого мы должны
# зависить от интерфейса этих классов (публичных методов)

# Getters/setters

# class Cat:
#     _name: str
#     _age: int
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, new_name):
#         new_name = new_name.strip()
#         self.name = new_name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, new_age):
#         self.age = new_age
#
# c = Cat()
# c.get_name()
#
#
# class A:
#     def __init__(self, another_class):
#         self.another_class = another_class
#
#     def get_value(self):
#         return self.another_class.value
#
# class B:
#     def __init__(self):
#         self.value = 1
#
# a = A(B())
# print(a.another_class.value)

# Паттерны проектирования

# Паттерны проектирования впервые появились как сборник решений типовых проблем
# в 1994 году в одноименной книге-справочнике

# Зачем нужны паттерны проектирования?
# Повторное использование решений
# Упрощение сложных задач
# Упрощение коммуникации
# Поддержка и развитие кода

# Три ключевые группы паттернов
# 1) Структурные - помогают организовать большой набор классов и объектов
# для создания структур, которые можно легко поддерживать
# 2) Порождающие паттерны - сосредоточены на том как создаются объекты
# и помогают абстрагировать процесс их создания
# 3) Поведенческие паттерны - фокусируются на взаимодействии объектов
# и способах управления их поведением

# Паттрен - решение задачи в контесте

# Стратегия

# Поведенческий паттерн, который позволяет определить семейство алгоритмов,
# инкапсулировать их в виде отдельных классов и делать их
# взаимозаменяемыми, Этот паттерн позволяет изменять поведение объекта
# во время исполнения кода

# Симулятор утиных прудов
# class Duck:
#     def quack(self):
#         print("quack")
#
# class FlyingBehavior:
#     def fly(self):
#         print("Утка летит")
#
# class RealDuck(Duck, FlyingBehavior): ...
#
# class MullardDuck(Duck, FlyingBehavior): ...
#
# class RubberDuck(Duck): ...

class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    @abstractmethod
    def display(self):
        pass


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Я лечу с крыльями")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Я не умею летать")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("Тишина")


class RealDuck(Duck):
    def display(self):
        print("Я настоящая утка")


class RubberDuck(Duck):
    def display(self):
        print("Я резиновая утка")


class WoodenDuck(Duck):
    def display(self):
        print("Я деревянная утка")


real_duck = RealDuck(FlyWithWings(), Quack())
real_duck.perform_fly()
real_duck.perform_quack()
real_duck.fly_behavior = FlyNoWay()
real_duck.perform_fly()

# Гибкость - мы можем легко изменять поведение уток в зависимости от
# их типа или обстоятельства, не изменяя основной код
# Масштабируемость - добавление новых видов уток или нового поведения
# (например, нового типа полета) не требует изменения или добавления
# новых классов
# Простота поддержки - мы избежали дублирования кода и можем менять
# алгоритмы, не затрагивая структуру программы

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_type, amount):
        if discount_type == "percentage":
            return self.price * amount
        elif discount_type == "fixed":
            return self.price - amount
        else:
            return self.price

product = Product("Продукт", 5000)
print(product.apply_discount("percentage", 0.9))
print(product.apply_discount("fixed", 1000))


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        ...


class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9


class FixedDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price):
        return price - 1000


class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price


class Product:
    def __init__(
            self,
            name,
            price: int,
            discount_strategy: DiscountStrategy
    ):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price(self):
        return self.discount_strategy.apply_discount(self.price)


product1 = Product("Товар1", 1000, PercentageDiscount())
print(product1.get_price())
product1.discount_strategy = FixedDiscountStrategy()
print(product1.get_price())

# Декоратор
# Наблюдатель
# Шаблон
# Фабрика
# Архитектурный стиль Model View Controller
