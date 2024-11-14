class Monster:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = 30 * level
        self.attack = 5 * level
        self.defense = 3 * level

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)
