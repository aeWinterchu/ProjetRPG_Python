class Combat:
    def __init__(self, player, monster, inventory):
        self.player = player
        self.monster = monster
        self.inventory = inventory

    def start(self):
        print(f"A battle begins between {self.player.name} and {self.monster.name}!")
        
        while self.player.is_alive() and self.monster.is_alive:
            action = input("Choose an action: [Attack, Use Item, Run] ").lower()
            
            if action == "attack":
                self.player.attack_enemy(self.monster)
                if not self.monster.is_alive:
                    print(f"{self.monster.name} has been defeated!")
                    self.player.gain_xp(20)
                    break
                self.monster.attack_enemy(self.player)
                if not self.player.is_alive():
                    print("You have been defeated!")
                    break

            elif action == "use item":
                self.inventory.use_item(self.player)

            elif action == "run":
                print("You ran away from the battle!")
                break

            else:
                print("Invalid action. Please choose again.")

        self.player.end_combat()
