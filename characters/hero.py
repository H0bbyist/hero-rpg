from characters.base import Character
import random

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
        item.apply(self)
    
    def attack(self, enemy):
        crit_hit = random.random() > 0.8
        if crit_hit:
            print("The Hero has made a critical hit!")
            self.power *= 2
        super(Hero, self).attack(enemy)
        if crit_hit:
            self.power *= 0.5
