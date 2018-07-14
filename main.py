# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# - гусей "Серый" и "Белый"
# - корову "Маньку"
# - овец "Барашек" и "Кудрявый"
# - кур "Ко-Ко" и "Кукареку"
# - коз "Рога" и "Копыта"
# - и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# - кормить
# - корову и коз доить
# - овец стричь
# - собирать яйца у кур, утки и гусей
# - различать по голосам(коровы мычат, утки крякают и т.д.)

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

    def voice(self):  # метод который будет определять животное по голосу
        pass

    def get_food(self, value):  # метод кормить
        self.fullness += value
        print("{} по имени {} была покормлена. Уровень сытости {}".format(self.kind, self.name, self.fullness))


class Bird(Animals):  # птицы

    kind = ""

    def get_eggs(self):  # собирать яйцо
        print("{} по имени {} собрали яйцо.".format(self.kind, self.name))


class CowGoat(Animals):  #корова, коза

    kind = ""
    milk = 0

    def get_milk(self):  #доить
        print("{} по имени {} была подоена".format(self.kind, self.name))



class Sheep(Animals):  #овца

    def cut(self):  #подстригать
        pass

# Курица Ко-Ко
chicken_1 = Bird()
chicken_1.kind = "Курица"
chicken_1.name = "Ко-ко"
chicken_1.weight = 1

# Курица Кукареку
chicken_2 = Bird()
chicken_2.kind = "Курица"
chicken_2.name = "Кукареку"
chicken_1.weight = 1.5

# гусь Серый
goose1 = Bird()
goose1.kind = "Гусь"
goose1.name = "Серый"
goose1.weight = 3

# гусь Белый
goose2 = Bird()
goose2.kind = "Гусь"
goose2.name = "Белый"
goose2.weight = 5

# корова Манька
cow = CowGoat()
cow.kind = "Корова"
cow.name = "Манька"
cow.weight = 200

# коза Рога
goat_1 = CowGoat()
goat_1.kind = "Коза"
goat_1.name = "Рога"
goat_1.weight = 50

# коза Копыта
goat_2 = CowGoat()
goat_2.kind = "Коза"
goat_2.name = "Копыта"
goat_2.weight = 43

# утка Кряква
duck = Bird()
duck.kind = "Утка"
duck.name = "Кряква"
duck.weight = 0.5

# овца Барашек
sheep_1 = Sheep()
sheep_1.name = "Барашек"
sheep_1.weight = 45

# овца Кудрявый
sheep_2 = Sheep()
sheep_2.name = "Кудрявый"
sheep_2.weight = 33









