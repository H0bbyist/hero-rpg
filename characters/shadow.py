from characters.base import Character

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