from math import *
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def alive(self):
        if self.health > 0:
            return True
    def attack(self, enemy):
        enemy.health -= self.power
    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    

class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


hero = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)
zombie = Zombie("Zombie", float(inf), 100)
    
en = goblin
    
while en.alive() and hero.alive():
        print()
        hero.print_status()
        en.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(en.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do {} damage to the {}.".format(hero.power,en.name))
            if en.health <= 0:
                print("The {} is dead.".format(en.name))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("What kind of hero runs?")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if en.health > 0:
            # Goblin attacks hero
            en.attack(hero)
            print("The {} does {} damage to you.".format(en.name, en.power))
            if hero.health <= 0:
                print("You are dead.")

