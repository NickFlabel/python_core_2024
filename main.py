class A: ...
class B: ...

import random
from random import randint

list_of_classes = [A, B]
grid = []
for i in range(3):
    random_choice = random.choice(list_of_classes)
    initialized_obj = random_choice()
    grid.append(initialized_obj)
print(grid)
# Тимофей Хирьянов

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def interact(self):
        ...

class Item(GameObject):
    def interact(self):
        print("Вы подобрали предмет!")


dict_eng_to_rus = {
    "world": "мир"
}
dict_eng_to_rus["world"] # мир

dict_rus_to_eng = {} # "мир": "world"
for key, value in dict_eng_to_rus.items():
    dict_rus_to_eng[key] = value
