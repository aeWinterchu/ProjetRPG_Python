class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to your inventory.")

    def use_item(self, player):
        if not self.items:
            print("Your inventory is empty.")
            return
        
        # Afficher les items disponibles et permettre au joueur de choisir
        print("Choose an item to use:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        
        choice = int(input("Enter the number of the item to use: ")) - 1
        
        if 0 <= choice < len(self.items):
            item = self.items.pop(choice)
            if item == "Health Potion":
                player.restore_health(100)
                print("You used a Health Potion and restored 100 HP!")
            elif item == "Attack Boost":
                player.attack += 5
                player.attack_boost_active = True
                print("You used an Attack Boost! Attack increased for this combat.")
            elif item == "Defense Boost":
                player.defense += 5
                player.defense_boost_active = True
                print("You used a Defense Boost! Defense increased for this combat.")
        else:
            print("Invalid choice.")
