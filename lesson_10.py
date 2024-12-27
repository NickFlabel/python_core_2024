# Удаление неприемлимых слов из текста

# Открыть -> прочесть -> превратить в list ->
# проверить цикклом -> записать новый текст

def remove_unacceptable_words(original_file, unacceptable_words):
    with open(unacceptable_words, encoding="utf-8") as f:
        forbidden_words = set(line.strip() for line in f)

    with open(original_file, encoding="utf-8") as f:
        original_lines = f.readlines()

    with open(original_file, "w", encoding="utf-8") as f:
        for line in original_lines:
            words = line.split()
            for word in words:
                if word in forbidden_words:
                    pass
                f.write(word)

# Транслитерация
cirillic_to_latin = {"a": "a", "б": "b", "в": "v"}

text = "мой текст"
transliterated_result = ''.join(cirillic_to_latin.get(char) for char in text)

def transliterate(text, cirillic_to_latin=True):
    if cirillic_to_latin:
        with open("cirillic_to_latin.txt", encoding="utf-8") as f:
            cirillic_to_latin_dict = {}
            line = f.readline()
            while line:
                key_value_pair = line.split(":")
                cirillic_to_latin_dict[key_value_pair[0]] = key_value_pair[1]
                line = f.readline()
            return ''.join(cirillic_to_latin_dict.get(char) for char in text)
    else:
        with open("cirillic_to_latin.txt", encoding="utf-8") as f:
            cirillic_to_latin_dict = {}
            line = f.readline()
            while line:
                key_value_pair = line.split(":")
                cirillic_to_latin_dict[key_value_pair[1]] = key_value_pair[0]
                line = f.readline()
            return ''.join(cirillic_to_latin_dict.get(char) for char in text)

# Объединение содержимого файлов
def merge_files():
    file_names = []
    while True:
        file_name = input("Введите название файла: ")
        if file_name.lower() == "quit":
            break
        file_names.append(file_name)

    with open("merged_file.txt", "w", encoding="utf-8") as outfile:
        for file_name in file_names:
            try:
                with open(file_name, encoding="utf-8") as infile:
                    outfile.write(infile.read())
            except FileNotFoundError:
                print(f"Файл с именем {file_name} не найден")

# Поиск символов
def common_symbols():
    file_names = []
    while True:
        file_name = input("Введите название файла: ")
        if file_name.lower() == "quit":
            break
        file_names.append(file_name)

    common_chars = None
    for file_name in file_names:
        with open(file_name, encoding="utf-8") as f:
            file_chars = set(f.read())
            if common_chars is None:
                common_chars = file_chars
            else:
                common_chars = common_chars & file_chars

    if common_chars:
        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(str(common_chars))
