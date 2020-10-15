# Note that player stats are stored in this order: 
# name, health, max health, strength, power, defense, accuracy, and speed
# ---------------------------
# Item's information are stored as followed:
# name, effect, intensity, description

import json
#name, health, str, pow, def, acr, and spd
warrior = ["Warrior", 25, 15, 5, 15, 5, 5]
wizard = ["Wizard", 20, 5, 20, 5, 15, 5]
vagrant = ["vagrant", 15, 5, 5, 5, 15, 30]

classes = [warrior, wizard, vagrant]

def new_game():
    """will be used to create a new character"""
    print("Pick your class: ")
    print("warrior - A warrior with high strength and defense, and decent health.")
    print("wizard - A magister with high magical power and accuracy.")
    print("vagrant - A wanderer with low health, but high accuracy and speed.")
    return None

def load_game():
    """will be used to load a game"""
    data_chunk = []
    with open("saved_game.json", "r") as save_file:
        data_chunk.append(json.load(save_file))
    return data_chunk