import random

def calculate_damage(attack, defense):
    damage = max(attack - defense, 0)
    # Add randomness for critical hit or miss
    if random.random() < 0.1:  # 10% chance of critical hit
        damage *= 2
        print("Critical hit!")
    elif random.random() < 0.1:  # 10% chance of miss
        damage = 0
        print("Missed!")
    return damage
