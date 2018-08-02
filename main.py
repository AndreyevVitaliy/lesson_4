# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# - + гусей "Серый" и "Белый"
# - + корову "Маньку"
# - + овец "Барашек" и "Кудрявый"
# - + кур "Ко-Ко" и "Кукареку"
# - + коз "Рога" и "Копыта"
# - + и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# - + кормить
# - + корову и коз доить
# - + овец стричь
# - + собирать яйца у кур, утки и гусей
# - + различать по голосам(коровы мычат, утки крякают и т.д.)

# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование,
# определить общие методы взаимодействия с животными и дополнить их в
# дочерних классах, если потребуется.

# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.


class Animals(object):
    weight = 0  # вес животного
    name = ""  # имя животного
    fullness = 0

    def get_voice(self):  # метод который будет определять животное по голосу
        user_input = input("Напишите звук, который вы слышали")
        if user_input.lower() == "му":
            print("Это корова")
        elif user_input.lower() == "бе":
            print("Это баран")
        elif user_input.lower() == "ме":
            print("Это коза")
        elif user_input.lower() == "кря":
            print("Это утка")
        elif user_input.lower() == "га":
            print("Это гусь")
        elif user_input.lower() == "ко":
            print("Это курица")

    def get_food(self, value):  # метод кормить
        self.fullness += value
        print("{} по имени {} была покормлена. Уровень сытости {}".format(self.kind, self.name, self.fullness))

    def __init__(self, name, weight):
        self.weight = weight
        self.name = name
        all_animal.append({"name":self.name, "weight":self.weight})


class Bird(Animals):  # птицы

    def get_eggs(self):  # собирать яйцо
        print("{} по имени {} собрали яйцо.".format(self.kind, self.name))

class Goose(Bird):  # Гусь

    kind = ""

class Chicken(Bird): #Курица

    kind = ""
    
class Duck(Bird):

    kind = ""


class Cow(Animals):  # корова, коза

    kind = ""
    milk = 0

    def get_milk(self):  # доить
        print("{} по имени {} была подоена".format(self.kind, self.name))

class Goat(Animals):  # корова, коза

    kind = ""
    milk = 0

    def get_milk(self):  # доить
        print("{} по имени {} была подоена".format(self.kind, self.name))



class Sheep(Animals):  # овца

    def get_cut(self):  # подстригать
        print("Овца по имени {} была подстрижена".format(self.name))


all_animal = []

# Курица Ко-Ко
chicken_1 = Chicken("Ко-ко", 1)
chicken_1.kind = "Курица"

chicken_1.get_eggs()

# Курица Кукареку
chicken_2 = Chicken("Кукареку", 1.5)
chicken_2.kind = "Курица"

# гусь Серый
goose1 = Goose("Серый", 4)
goose1.kind = "Гусь"

goose1.get_eggs()

# гусь Белый
goose2 = Goose("Белый", 5)
goose2.kind = "Гусь"

goose2.get_food(1)

# корова Манька
cow = Cow("Манька", 200)
cow.kind = "Корова"

cow.get_milk()

# коза Рога
goat_1 = Cow("Рога", 50)
goat_1.kind = "Коза"

goat_1.get_milk()

# коза Копыта
goat_2 = Goat("Копыта", 43)
goat_2.kind = "Коза"

goat_2.get_milk()

# утка Кряква
duck = Duck("Кряква", 0.5)
duck.kind = "Утка"

duck.get_eggs()

# овца Барашек
sheep_1 = Sheep("Барашек", 45)

sheep_1.get_cut()

# овца Кудрявый
sheep_2 = Sheep("Кудрявый", 33)

# sheep_2.get_voice()

max_weight = 0
name_animal = ""
for animal in all_animal:
    if animal["weight"] > max_weight:
        max_weight = animal["weight"]
        name_animal = animal["name"]

print("Животное с максимальным весом {} его вес {}".format(name_animal, max_weight))
