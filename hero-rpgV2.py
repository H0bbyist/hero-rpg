import random
import time
import os

from characters.goblin import Goblin
from characters.hero import Hero
from characters.wizard import Wizard
from characters.medic import Medic
from characters.shadow import Shadow
from characters.zombie import Zombie


class Battle:
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

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print("{}'s power increased to {}.".format(character.name, character.power))

class SuperTonic:
    cost = 20
    name = 'supertonic'
    def apply(self, character):
        character.health += 10
        print("{}'s power increased to {}.".format(character.name, character.health))

class Armor:
    cost = 15
    name = 'armor'
    def apply(self, character):
        character.armor += 2
        print("{}'s armor is increased to {}".format(character.name, character.armor))


class Store:
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