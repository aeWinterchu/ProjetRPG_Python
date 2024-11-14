class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        self.xp = 0
        self.xp_to_next_level = 100
        self.attack_boost_active = False
        self.defense_boost_active = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp -= actual_damage
        print(f"{self.name} took {actual_damage} damage and has {self.hp} HP left.")

    def restore_health(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} restored {amount} HP. Current HP: {self.hp}")

    def gain_xp(self, xp_gained):
        self.xp += xp_gained
        print(f"{self.name} gained {xp_gained} XP!")
        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)  
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"Stats increased! HP: {self.max_hp}, Attack: {self.attack}, Defense: {self.defense}")

    def attack_enemy(self, monster):
        damage = max(0, self.attack - monster.defense)
        monster.take_damage(damage)
        print(f"{self.name} attacked {monster.name} for {damage} damage.")

    def end_combat(self):
        if self.attack_boost_active:
            self.attack -= 5
            self.attack_boost_active = False
        if self.defense_boost_active:
            self.defense -= 5
            self.defense_boost_active = False
        print("Combat effects reset.")
