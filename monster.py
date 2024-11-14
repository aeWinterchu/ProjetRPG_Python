class Monster:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = 50 + level * 10
        self.attack = 8 + level * 2
        self.defense = 3 + level
        self.is_alive = True

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} damage and has {self.hp} HP left.")
        if self.hp <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, player):
        damage = max(0, self.attack - player.defense)
        player.take_damage(damage)
        print(f"{self.name} attacked {player.name} for {damage} damage.")
