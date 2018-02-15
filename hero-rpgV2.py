import random
import time
import os

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.armor = 0
        self.power = 5
        self.coins = 20
        self.items = []
        
    def receive_damage(self, points):
        damage = points - self.armor
        if damage < 0:
            damage = 0
          
        self.health -= damage
        print("{} has {} armor.".format(self.name, self.armor))
        print("{} received {} damage.".format(self.name, damage))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def restore(self):
        self.health = 10
        print("Hero's health is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)
    
    def attack(self, enemy):
        crit_hit = random.random() > 0.8
        if crit_hit:
            print("The Hero has made a critical hit!")
            self.power *= 2
        super(Hero, self).attack(enemy)
        if crit_hit:
            self.power *= 0.5
        
class Medic(Character):
    def __init__(self): 
        self.name = "Medic"
        self.health = 10
        self.power = 3
        self.prize = 5
    
    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        h_boost = random.random() > 0.8
        if h_boost:
            self.health += 2
            print("Medic got health boost and gained 2 health!")

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 7
        self.power = 3
        self.prize = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 8
        self.power = 4
        self.prize = 10

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Shadow(Character):
    def __init__(self):
        self.name = "Shadow"
        self.health = 1
        self.power = 5
        self.prize = 3

    def receive_damage(self, points):
        dodge = random.random() > 0.9
        if not dodge:
            print("Attack passed right through the shadow!")
        else:
            super(Shadow, self).receive_damage(points)

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 5
        self.power = 1
        self.prize = 0
    
    def alive(self):
        return True
    
    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is already dead.".format(self.name))
        

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("4. quit game")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                break
            elif keyinput == 4:
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            hero.coins += enemy.prize
            print("The hero has found", enemy.prize, "coins!")
            return True
            
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print("{}'s power increased to {}.".format(character.name, character.power))

class SuperTonic(object):
    cost = 20
    name = 'supertonic'
    def apply(self, character):
        character.health += 10
        print("{}'s power increased to {}.".format(character.name, character.health))

class Armor(object):
    cost = 15
    name = 'armor'
    def apply(self, character):
        character.armor += 2
        print("{}'s armor is increased to {}".format(character.name, character.armor))


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor]
    def do_shopping(self, hero):
        while True:
            os.system('clear')
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("The Hero's health is", hero.health)
            print("The Hero's power is", hero.power)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            keyinput = int(input("> "))
            print(keyinput)
            if keyinput == 10:
                break
            else:
                ItemToBuy = Store.items[keyinput - 1]
                item = ItemToBuy()
                hero.buy(item)
                time.sleep(1.5)

if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard(), Zombie(), Shadow()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)  
        shopping_engine.do_shopping(hero)
        os.system('clear')


    print("YOU WIN!")