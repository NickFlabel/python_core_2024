lst = [1, 2]

try:
    int("hello")
    lst[10] == 1
except (ZeroDivisionError, IndexError):
    print("Код был с ошибкой")
except ValueError:
    print("Возникла ValueError")

print("Код после деления на ноль")