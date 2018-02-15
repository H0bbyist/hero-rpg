from characters.base import Character

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