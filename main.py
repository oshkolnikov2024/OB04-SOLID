### Шаг 1: Абстрактный класс для оружия

from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


### Шаг 2: Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")


### Шаг 3: Модификация класса `Fighter`

class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon

    def fight(self, monster):
        print("Боец выбирает", type(self.weapon).__name__ + ".")
        self.weapon.attack()
        print(monster.get_defeated())

### Шаг 4: Класс `Monster` и механизм сражения

class Monster:
    @staticmethod
    def get_defeated():
        return "Монстр побежден!"


# Демонстрация механизма сражения
def battle_demo():
    monster = Monster()
    # Боец с мечом
    fighter_with_sword = Fighter(Sword())
    fighter_with_sword.fight(monster)
    # Боец сменит на лук
    fighter_with_sword.changeWeapon(Bow())
    fighter_with_sword.fight(monster)


battle_demo()

# Этот код демонстрирует применение принципа открытости / закрытости.Если нам потребуется
# добавить новый тип оружия, например, магический посох, нам просто надо будет создать еще один
# класс, наследованный от `Weapon`, и реализовать метод `attack()`, не изменяя при этом существующие классы
# `Fighter` и `Weapon`.

### Добавление нового оружия (Пример)

class MagicStaff(Weapon):
    def attack(self):
        print("Боец высвобождает магическую энергию посоха.")

