from player import Player
from game_map import GameMap
from combat import Combat
from monster import Monster
from inventory import Inventory

def main_menu():
    while True:
        print("-------------------")
        print("Main Menu:")
        print("1. Create New Game")
        print("2. Load Saved Game (not available in this version)")
        print("3. About")
        print("4. Exit")
        print("-------------------")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            start_game()
        elif choice == "2":
            print("Load Saved Game is not available in this version.")
        elif choice == "3":
            print("RPG Game - A retro-style RPG game where you explore, battle monsters, and level up!")
        elif choice == "4":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def start_game():
    name = input("Enter your character's name: ")
    player = Player(name)
    game_map = GameMap()
    player_inventory = Inventory()
    
    while player.is_alive():
        print(game_map.get_current_location())
        action = input("What do you want to do? [go north, go south, go east, go west, quit] ").lower()
        if action.startswith("go"):
            game_map.move(action, player)
            
            # Rencontre de monstre
            monster_info = game_map.encounter_monster()
            if monster_info:
                monster = Monster(monster_info["name"], level=monster_info["level"])
                print(f"A wild {monster.name} appeared!")
                Combat(player, monster, player_inventory).start()

            # Trouver un objet
            item = game_map.find_item()
            if item:
                print(f"You found a {item}!")
                player_inventory.add_item(item)

        elif action == "quit":
            print("Exiting to main menu.")
            break
            
    print("Game Over.")

# Exécution du menu principal au démarrage
if __name__ == "__main__":
    main_menu()
