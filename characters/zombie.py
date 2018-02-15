from characters.base import Character

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