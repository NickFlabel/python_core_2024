# Текстовые файлы/текстовые потоки
# текстовый поток - последовательность символов
# При переводе из потока на экран часть из них
# на него не выводится

# Бинарный поток/бинарные файлы
# Любое расширение, кроме .txt это - бинарный код
# Если у нас есть .mp3 файл, то он содержит как раз
# бинарный код и считывать его обычными методами
# будет невозможно

# методы для чтения бинарного файла
# бинарные методы подразумевают добавление буквы b
# к уже известным вам методам

file = open("my_binary", "wb")
file.write(b"my_str") # b перед str переводит строку в
# двоичный код. При записи в бинарный файл python
# требует передачи byte-like object или иными словами
# данные, переденные в двоичный код

file = open("my_binary", "rb")
content = file.read()
print(content)
file.close() # Метод close() дает python'у знать,
# что мы закончили работу с файлом и теперь он может
# освободить все ресурсы, выделенные на его обработку при
# открытии файла

# Менеджер контекста
# with open("files/example.txt", "w") as file:
#     file.write("Новая информация")

# после окончания блока с отступами file вызовет метод
# close()

# Многие объекты в python умеют взаимодействовать с
# ключевым словом with
# Это взаимодействие проиходит следующим образом:
# Объект делает что-то при входе (как правило просто
# создает новую переменную)
# Объект делает что-то при выходе (после отступов

# with "string": # приводит к ошибке - тип данных str
# # не поддерживет протокол менеджера контекста
#     print("string")
# У типа данных str нет метода __enter__() и __exit__()

# Когда мы вызываем какой-то объект с ключевым словом
# with мы по сути вызывем у него метод .__enter__()
# и после блока кода - метод .__exit__()

# file = open("files/example.txt", "r")
# file.__exit__() # этот метод по сути - close() и он вызывается
# после того как код в менеджере контекста был исполнен

# Ключевое слово with позволяет нам создать блок кода,
# называемый менеджером контекста и затем быть уверенными,
# что предаваемый в менеджер объект выполнит какую-то
# работу

# with open("files/example.txt", "w", encoding="utf-8") as file:
#     file.write("new data")
# file.close()

# Задание №1: у нас есть текстовый файл и нам необходимо
# заменить каждое вхождение слова Python на JavaScript


def replace_text_in_file(file_name, original_text, new_text):
    with open(file_name, encoding="utf-8") as file:
        data = file.read() # после метода read мы сохраняем str
        data = data.replace(original_text, new_text)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(data)

# my_file = "files/example.txt"
# replace_text_in_file(my_file, "Python", "JavaScript")


# Подсчитать количество слов в текстовом файле,
# которые не являются числами

def word_counter(file_name):
    number_of_words = 0
    with open(file_name, encoding="utf-8") as file:
        data = file.read()
        lines = data.split()
        for word in lines:
            if not word.isnumeric():
                number_of_words += 1

    print("Количество слов в файле: ", number_of_words)
        # line = file.readline()
        # while line:
        #     print(line)
        #     line = file.readline()


# word_counter("files/example.txt")

# дан текстовый файл, необходимо удалить n-ую строку из него

def remove_line(file_name, n):
    with open(file_name, encoding="utf-8") as file:
        lines = file.readlines()
    with open(file_name, "w", encoding="utf-8") as file:
        line_counter = 1
        for line in lines:
            if line_counter != n:
                file.write(line)
            line_counter += 1

remove_line("files/example.txt", 2)
