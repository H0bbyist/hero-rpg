from characters.base import Character
import random

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