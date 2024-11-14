import random

class GameMap:
    def __init__(self):
        # Carte étendue avec des descriptions pour chaque position
        self.map = {
            (0, 0): "You are at the starting point. The forest is dense around you.",
            (0, 1): "A peaceful forest clearing. Sunlight breaks through the trees.",
            (1, 0): "A dark cave entrance. It looks ominous.",
            (-1, 0): "An ancient stone shrine covered in moss.",
            (0, -1): "A narrow river flows here. The water is crystal clear.",
            (1, 1): "A small meadow filled with flowers. You feel at ease.",
            (-1, -1): "A dense thicket. It's difficult to see far ahead.",
            (2, 0): "A steep hill. From here, you can see more of the forest.",
            (-2, 0): "A grove of ancient trees. It feels sacred here.",
            (0, 2): "A deep pond with rippling water.",
            # ...
        }
        self.player_position = (0, 0)
        self.items = ["Potion", "Attack Boost", "Defense Boost"]
        self.monsters = [
            {"name": "Goblin", "level": 1},
            {"name": "Wolf", "level": 2},
            {"name": "Orc", "level": 3},
            {"name": "Troll", "level": 4},
            {"name": "Dragon", "level": 5},  # Boss
        ]
        self.boss_position = (2, 2)  # Position du boss pour une bataille finale

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
        # Vérifie si le joueur a atteint la position du boss
        if self.player_position == self.boss_position:
            print("You feel an ominous presence... The Boss is here!")

    def encounter_monster(self):
        # Ne pas rencontrer de monstres au point de départ ou à l'emplacement du boss
        if self.player_position == (0, 0) or self.player_position == self.boss_position:
            return None
        # 30% de chance de rencontrer un monstre
        if random.random() < 0.3:
            monster_info = random.choice(self.monsters)
            return monster_info
        return None

    def find_item(self):
        # Ne pas trouver d'objets au point de départ ni au boss
        if self.player_position == (0, 0) or self.player_position == self.boss_position:
            return None
        # 40% de chance de trouver un objet
        if random.random() < 0.4:
            return random.choice(self.items)
        return None
