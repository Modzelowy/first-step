# klasy i obiekty
# obiekt to pojemnik na     pojemniki i funkcje
# vary i defy xd
# obiekt ma lokalny scope tylko dla siebie podobnie jak w funkcjach
# vary w obiekcie to atrybuty
# funkcje w obiekcie to metody


# klasy
# by stworzyc obiekt pierw musisz miec klsae
# klasa moze zmieniac obiekt i tworzyc go
# klasa moze korzystac  z innej zeby zabrac jej funkcjonalność
# wtedy ów klasa ma i swoje unikalne dla siebie + inne z tej z której rozkradła


# klasy towrzymy z CamelCase


# class Monster:
#    # attributes
#    health = 90
#    energy = 40

#    def __init__(self, health, energy):
#        self.health = health
#        self.energy = energy

# methods
# method needs at least one parameter
#   def attack(self, amount):
#       print("the monster has attacked")
#       print(f"{amount} damage was dealt")
#
#   def move(self, move):
#        print(f"monster has moved with the speed of {move}")

#   def __str__(self):
#       return f"health {self.health} energy {self.energy}"


# monster = Monster()
# monster.attack(40)
# monster.move(10)


# Dunder = double underscore methods

# monster1 = Monster(10, 20)
# monster2 = Monster(health=50, energy=50)
# print(monster1)


# create a Monster class with a parameter called func, store this func as parameter
# class Monster:
#    def __init__(self, func):
#        self.func = func
#

# create another class, called Attacks, that has 4 methods:
# bite, strike, slash, kick (each method just prints some text)
# class Attacks:
#    def bite(self):
#        print("MONSTER BITED YOU FOR 999")
#
#    def slash(self):
#        print("MONSTER SLASHED YOU FOR 9999")
#
#    def strike(self):
#        print("Monster striked u for inifnity dmg striked u down xd")
#
#    def kick(self):
#        print("Monster kicked u for 2 dmg not very effective")

# attacks = Attacks()
# monster = Monster(func=attacks.bite)
# monster.func()
# monster2 = Monster(func=attacks.strike)
# # create a monster object and give it on`e of the attack
# monster2.func() """
# class Monster:
#     def __init__(self, health, energy):
#         self.health = health
#         self.energy = energy

#     def get_dmg(self, amount):

#         self.health -= amount


# class Hero:
#     def __init__(self, damage, monster):
#         self.damage = damage
#         self.monster = monster

#     def attack(self):
#         self.monster.get_dmg(self.damage)


# monster = Monster(100, 50)

# hero = Hero(damage=20, monster=monster)
# print(monster.health)
# hero.attack()
# print(monster.health)


# class Monster:
#     def __init__(self, health, energy):
#         self.health = health
#         self.energy = energy

#     # methods
#     def attack(self, amount):
#         print("The monster has attacked!")
#         print(f"{amount} damage was dealt")
#         self.energy -= 20

#     def move(self, speed):
#         print("The monster has moved")
#         print(f"It has a speed of {speed}")


# # exercise
# # create scorpion class that inherits from monster
# # health and energy from the parent
# # poison_damage attribute
# # overwrite the damage method to show poison damage


# class Scorpion(Monster):
#     def __init__(self, poison_damage, health, energy):
#         super().__init__(health, energy)
#         self.poison_damage = poison_damage

#     def attack(self):
#         print(f"The scorpion has attacked")
#         print(f"Dealing a massive poison damage of {self.poison_damage}")


# scorpion = Scorpion(100, 30, 25)
# print(scorpion.health)
# scorpion.attack()
