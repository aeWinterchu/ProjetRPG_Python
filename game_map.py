import random

class GameMap:
    def __init__(self):
        self.map = {
            (0, 0): "You are at the starting point.",
            (0, 1): "A forest clearing. It’s quiet...",
            (1, 0): "A dark cave looms ahead.",
            # Define more locations
        }
        self.player_position = (0, 0)

    def get_current_location(self):
        return self.map.get(self.player_position, "Unknown location")

    def move(self, direction, player):
        x, y = self.player_position
        if direction == "go north":
            self.player_position = (x, y + 1)
        elif direction == "go south":
            self.player_position = (x, y - 1)
        elif direction == "go east":
            self.player_position = (x + 1, y)
        elif direction == "go west":
            self.player_position = (x - 1, y)
        else:
            print("Invalid direction.")
        print(self.get_current_location())

    def encounter_monster(self):
        # 30% chance to encounter a monster in each move
        return random.random() < 0.3
