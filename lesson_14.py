# Создание системы для управления зоопарком
# В зоопарке есть разные виды животных,
# каждый из которых имеет свои уникальные характеристики
# и поведение
# Также у зоопарка есть сотрудники, которые
# ухаживают за животными

# Создать главный класс Zoo
# Создать классы для Animal и Employee

# Zoo
# - данные о всех сотрудниках
# - данные о всех животных
# - метод, отвечающие за его функционирование

# Employee
# - имя
# - метод при помощи которого он ухаживает за животными

# Animal
# - название
# - метод для издавания звука

class Animal:
    _sound = "undefined"

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"Sound: {self._sound}")

class Dog(Animal):
    _sound = "bark"

class Monkey(Animal):
    _sound = "monkey sound"

class Fish(Animal):
    _sound = "None"


class Employee:
    def __init__(self, name):
        self.name = name

    def perform_duties(self):
        print(f"Работник ухаживает за животными")


class Zoo:
    def __init__(self, employees, animals):
        self.employees = employees
        self.animals = animals

    def daily_routine(self):
        for employee in self.employees:
            employee.perform_duties()
        for animal in self.animals:
            animal.make_sound()


dog = Dog("dog")
fish = Fish("fish")
monkey = Monkey("monkey")

worker_1 = Employee("name 1")
worker_2 = Employee("name 2")

zoo = Zoo([worker_1, worker_2], [dog, fish, monkey])
zoo.daily_routine()

# Реализация игры "Три в ряд"
# Создать консольную версию игры "Три в ряд", где пользователь
# сможет перемещать элементы на игровом поле и заработывать очки
# за совпадения

# Игровая ячейка - простейший элемент игрового поля, который
# содержит какое-то значение

# Игровое поле - объект, который будет содержать в себе
# текущее состояние игрового поля и реализовывать методы для
# перемещения ячеек

# Игрок - сущность, содержащая в себе текущие очки

class Cell:
    def __init__(self, value): # value - цифра, буква или символ
        # в ячейке. Представляет собой именно то, что нам нужно
        # собрать три в ряд
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.symbols = ["A", "B", "C", "D", "E", "F", "G"]
        self.grid = [] # [["A", "B"], ["C", "A"]]

    def initialize_grid(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                value = random.choice(self.symbols)
                row.append(Cell(value))
            self.grid.append(row)

    def display(self):
        for row in self.grid:
            print("|".join(str(cell) for cell in row))

    def find_matches(self):
        matches = []

        # Горизонтальные совпадения
        for y in range(self.height):
            for x in range(self.width - 2): # [["a", "b", "c"]]
                if (self.grid[y][x].value == self.grid[y][x+1].value == self.grid[y][x+2].value):
                    matches.append((y, x))
                    matches.append((y, x+1))
                    matches.append((y, x+2))

        # Вертикальные совпадения
        for x in range(self.width):
            for y in range(self.height - 2):
                if (self.grid[y][x].value == self.grid[y+1][x].value == self.grid[y+2][x].value):
                    matches.append((y, x))
                    matches.append((y+1, x))
                    matches.append((y+2, x))

        # Убрать дублирующиеся совпадения, чтобы не повторялись
        # координаты
        unique_matches = []
        for match in matches:
            if match not in unique_matches:
                unique_matches.append(match)

        return unique_matches

    def count_score(self, unique_matches):
        return len(unique_matches)

    def clear_matches(self, unique_matches):
        for y, x in unique_matches:
            self.grid[y][x] = None

    def fill_empty_cells(self):
        for x in range(self.width):
            column = []
            for y in range(self.height):
                if self.grid[y][x] is not None:
                    column.append(self.grid[y][x])

            empty_column = self.height - len(column)
            for i in range(empty_column):
                column.insert(0, Cell(random.choice(self.symbols)))

            for y in range(self.height):
                self.grid[y][x] = column[y]

    def swap_cells(self, x1, y1, x2, y2):
        # Проверить соседство
        if abs(int(x1) - int(x2)) + abs(int(y1) - int(y2)) != 1:
            print("Можно менять местами только соседние элементы")
            return

        self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = Board(width, height)
        self.board.initialize_grid()
        self.score = 0

    def game_turn(self):
        self.board.display()
        print(f"Ваши очки: {self.score}")
        x1 = int(input("Введите x-координату первой ячейки"))
        y1 = int(input("Введите y-координату первой ячейки"))
        x2 = int(input("Введите x-координату второй ячейки"))
        y2 = int(input("Введите y-координату второй ячейки"))
        self.board.swap_cells(x1, y1, x2, y2)
        matches = self.board.find_matches()
        self.score += self.board.count_score(matches)
        self.board.clear_matches(matches)
        self.board.fill_empty_cells()

    def start(self):
        while True:
            self.game_turn()

game = Game(6, 6)
game.start()

# cell1 = Cell("A")
# cell2 = Cell("A")
# print(cell1 == cell2) # False
#@FlaviusBelisarius
# github.com/NickFlabel/python_core_2024

...
# 1, 1
class A: ...
class B: ...
import random
list_of_classes = [A, B]
grid = []
for i in range(3):
    grid.append(random.choice(list_of_classes))
print(grid)
