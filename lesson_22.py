# Стратегия

# Это паттерн проектирования, который определяет семейство алгоритмов,
# икпапсулирует их в отедльные классы и делает взаимозаменяемыми
# Этот паттерн позволяет динамически изменять поведение объекта,
# не меняя его код

# Когда мы используем этот паттерн?
# 1) Когда у объекта есть несколько вариантов поведения,
# которые могут изменяться во время выполнения
# 2) Когда нужно обработать множество условных операторов (if-else)
# 3) Когда нужно изолировать код конкретных алгоритмов от основного класса

# Интернет-магазин
# class PaymentProcessor:
#     def pay(self, amount, method):
#         if method == "card":
#             print(f"Оплачено {amount} при помощи карты")
#         elif method == "PayPal":
#             print(f"Оплачено {amount} при помощи PayPal")
#         elif method == "cryptocurrency":
#             print(f"Оплачено {amount} при помощи криптовалюты")
#         else:
#             print("Ошибка оплаты")

# Проблема: при добавлении нового метода оплаты придется изменять этот
# класс. Это нарушает принцип открытости/закрытости

from abc import abstractmethod


class PaymentStrategy:
    @abstractmethod
    def pay(self, amount):
        ...


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} при помощи карты")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} при помощи PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} при помощи криптовалюты")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

payment = PaymentProcessor(PayPalPayment())
payment.strategy = CardPayment()
payment.process_payment(100)


# Декоратор
# Это структурный паттерн, который позволяет динамически расширять
# функциональность объектов без изменения их кода
# Вместо наследования декоратор использует композицию

# Когда использвать?
# Когда нельзя или неудобно менять исходный код класса
# Когда нужно добавлять новый функционал на лету без создания
# множества подклассов
# Когда необходимо гибко комбинировать различные расширения объекта


class PaymentLoggingDecorated:
    def __init__(self, decorated_object):
        self.decorated_object = decorated_object

    def process_payment(self, amount):
        print("Операция по оплате начата")
        self.decorated_object.process_payment(amount)
        print("Операция по оплате завершена")


payment = PaymentProcessor(CardPayment())
payment = PaymentLoggingDecorated(payment)
payment = PaymentLoggingDecorated(payment)
payment.process_payment(100)


# Наблюдатель
# Наблюдатель позволяет объектам подписываться на события и получать
# уведомления при их изменении

class CurrencyExchange:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notify(self, rate):
        for subscriber in self.subscribers:
            subscriber.update(rate)

class Media:
    def update(self, rate):
        print(f"Новый курс: {rate}")

class Trader:
    def update(self, rate):
        if rate > 100:
            print("Продаю валюту")


trader = Trader()
media = Media()
exchange = CurrencyExchange()
exchange.subscribe(trader)
exchange.subscribe(media)
exchange.notify(50)
exchange.notify(100)
exchange.notify(150)
exchange.unsubscribe(trader)
exchange.notify(200)


# MVC (Model-View-Controller) - архитектурный стиль, который организует
# работу приложений, разделяя их на три основных компонента -
# модель (model), предтавление (view) и контроллер (controller)
# Каждая часть выполняет свою роль и вместе они обеспечивают
# независимость компонентов друг от друга

# Модель представляет собой бизнес-логику и данные приложения.
# В этом архитектурном стиле модель реализует
# паттерн Наблюдатель. Это позволяет ей уведмлять зарегистрированные
# объекты о произошедших изменениях

# View - представлени - отвечает за визуализацию данных, которые предоставляет
# модель. В классическом MVC представление (view) обновляет данные,
# когда получает уведомление об их изменении от модели

# Controller - контроллер управляет поведением приложения и взаимодействуте
# с моделью


# В создании такого рода приложений активным образом участвуют паттерны
# проектирования
# Модель уведомляет контроллер и view об изменения при помощи наблюдателя
# Контроллер можно вопспринимать как стратегию
# View являются наблюдателями по отношению к моделе

# Зачем мы используем MVC?

# Изоляция компонентов
# Гибкость
# Повторное использование
