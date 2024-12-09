# Задача №1
# Написать рекурсивную функцию, которая вычисляет
# сумму всех чисел в диапазоне от a до b
# с заданным шагом step

# Обычное решение
def sum_range(a, b, step): # с шагом 2 он будет считать
    # сумму: [1, 3, 5, 7, 9]
    total = 0
    for i in range(a, b, step):
        total += i
    return total

# Рекурсивное решение
def sum_range_recursive(a, b, step):
    # Базовый случай
    if a > b:
        return 0
    # Рекурсивный случай
    else:
        return a + sum_range_recursive(a + step, b, step)

print(sum_range_recursive(1, 10, 2)) # 25
# print(sum_range(1, 10, 2)) # 25

# Реверс строки
# Написать функцию, которая принимает строку и возвращает
# ее реверс

def reverse_string(s):
    new_str = ""
    for i in range(len(s) - 1, -1, -1):
        new_str += s[i]
    return new_str
    # return s[::-1]

def reverse_string_recursive(s):
    # Базовый случай
    if len(s) == 0:
        return ""
    # Рекурсивный случай
    return s[-1] + reverse_string_recursive(s[:-1])


print(reverse_string_recursive("hello")) # "olleh"

# Вывод последовательности символов
# Написать функцию, которая принимает число n и символ char,
# а затем выводит строку из n повторений этого символа

def print_chars(n, char):
    print(char * n)

def print_chars_recursive(n, char):
    # Базовый случай
    if n == 0:
        return
    # Рекурсивный случай
    print(char, end='')
    print_chars_recursive(n - 1, char)

# print_chars_recursive(5, "*")
# print_chars(5, "*") # *****

# Поиск минимального элемента в списке
# Написать функцию, которая находит минимальное число в списке


def find_min(lst):
    minimum = None
    for i in lst:
        if not minimum or minimum > i:
            minimum = i
    return minimum
    # return min(lst)

def find_min_recursive(lst):
    # Базовый случай
    if len(lst) == 1:
        return lst[0]
    # Рекурсивный случай
    # [1, 2]
    next_minimum = find_min_recursive(lst[1:]) # 2
    if lst[0] < next_minimum:
        return lst[0]
    else:
        return next_minimum


# Бинарный поиск

def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)

arr = [1, 10, 11, 14, 16, 20, 25]
print(binary_search(arr, 25, 0, len(arr) - 1)) # 7

# Задания 5 и 6 - дополнительные
def func(a, b, c, d):
    pass
lst = [1, 2, 3, 4]
func(*lst) # тоже самое lst(lst[0], lst[1]...)


# Написать рекурсивную функцию нахождения степени числа
def power(a, b):
    if b <= 0:
        return 1
    else:
        return a * power(a, b - 1)

# Рекурсивная функция для вывода суммы всех чисел
# в диапазоне от a до b
def sum_range(a, b):
    if a > b:
        return 0
    else:
        return sum_range(a + 1, b)

# Рекурсивная функция для вывода N звезд в ряд
def print_stars(n):
    if n > 0:
        print("*")
        print_stars(n - 1)

# Игра "крестики-нолики"
def print_board(board): # board - список, хранящий текущее
    # состояние стола
    for row in board: # board = [["x", "o", "x"]]
        print(" | ".join(row)) # ["x", "o", "x"] -> "x | o | x"
        print("-" * 5)

def check_winner(board):
    # проверка по вертикали
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return board[0][0] # Возвращает символ победителя
    # проверка по горизонтали
    if board[0][1] == board[0][1] == board[0][2] != " ":
        return board[0][1]
    # Дальше описать все возможные комбинации для победных символов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    return None

def is_full(board): # [["x", "o", "x"]] [[" ", " ", " "]]
    # Проверяет, заполнено ли поле для определения ничьи
    for row in board:
        for elem in row:
            if elem == " ":
                return False
    return True

def tic_tac_toe():
    # Создание игрового поля
    board = []
    for i in range(3):
        board.append([" " for j in range(3)])
    players = ["x", "o"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]

        print(f"Ход игрока {current_player}")
        move = input("Введите строку и столбец для вашего хода через пробел (0 1)")
        move_x = move.split()[0] # 2 0 -> ["2", "0"]
        move_y = move.split()[1]

        board[int(move_x)][int(move_y)] = current_player
        winner = check_winner(board)

        if winner:
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print("Ничья")
            break

        turn += 1

tic_tac_toe()
