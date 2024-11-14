from player import Player
from game_map import GameMap
from combat import Combat
from monster import Monster

def main_menu():
    print("""
    -------------------
    Main Menu:
    1. Create New Game
    2. Load Saved Game
    3. About
    4. Exit
    -------------------
    """)
    choice = input("Choose an option: ")
    return choice

def start_game():
    name = input("Enter your character's name: ")
    player = Player(name)
    game_map = GameMap()
    while player.is_alive():
        print(game_map.get_current_location())
        action = input("What do you want to do? [go north, go south, go east, go west, quit] ").lower()
        if action.startswith("go"):
            game_map.move(action, player)
        elif action == "quit":
            print("Exiting to main menu.")
            break
        # Other game logic like encountering monsters
        if game_map.encounter_monster():
            monster = Monster("Goblin", level=1)  # Example monster
            Combat(player, monster).start()
    print("Game Over.")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            start_game()
        elif choice == "4":
            print("Exiting the game.")
            break
