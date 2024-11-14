from utils import calculate_damage

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start(self):
        while self.player.is_alive() and self.monster.is_alive():
            action = input("Choose your action: [Attack, Use Item, Flee] ").lower()
            if action == "attack":
                damage = calculate_damage(self.player.attack, self.monster.defense)
                self.monster.take_damage(damage)
                print(f"You dealt {damage} damage to the {self.monster.name}.")
            elif action == "use item":
                # Implement item usage
                pass
            elif action == "flee":
                print("You fled the battle.")
                break
            if self.monster.is_alive():
                damage = calculate_damage(self.monster.attack, self.player.defense)
                self.player.take_damage(damage)
                print(f"The {self.monster.name} dealt {damage} damage to you.")
        if not self.player.is_alive():
            print("You were defeated!")
        elif not self.monster.is_alive():
            print(f"You defeated the {self.monster.name}!")
