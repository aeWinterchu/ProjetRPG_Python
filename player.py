class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.xp = 0
        self.inventory = []

    def gain_xp(self, amount):
        self.xp += amount
        # Check for level up logic

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)
