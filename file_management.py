# Note that player stats are stored in this order: 
# name, health, max health, strength, power, defense, accuracy, and speed
# ---------------------------
# Item's information are stored as followed:
# name, effect, intensity, description

import json
import helper
#name, health, max health, str, pow, def, acr, and spd
warrior = ["Warrior", 25, 25, 15, 5, 15, 5, 5]
wizard = ["Wizard", 20, 20, 5, 20, 5, 15, 5]
vagrant = ["wanderer", 15, 15, 5, 5, 5, 20, 25]

classes = [warrior, wizard, vagrant]
stats = []

def new_game(stats: list) -> list:
    """will be used to create a new character"""
    name = input("Please enter your name: ")
    while not name:
        name = input("Please enter your name: ")
    helper.clear()
    print("Pick your class: ")
    print("warrior - A warrior with high strength and defense, and decent health.")
    print("wizard - A magister with high magical power and accuracy.")
    print("wanderer - A wanderer with low health, but high accuracy and speed.")
    choice = input()
    choice = choice.lower()
    valid = True
    while valid == True:
        for i in classes:
            if choice == i[0].lower():
                stats.append(i)
                stats[0][0] = name
                stats.append([])
                valid = False
                break
        if valid == False:
            break
        print("Invalid input. Please enter in one of the following: ")
        print("warrior - A warrior with high strength and defense, and decent health.")
        print("wizard - A magister with high magical power and accuracy.")
        print("wanderer - A wanderer with low health, but high accuracy and speed.")
        choice = input()
    with open("saved_game.json", "w") as save_file:
        json.dump(stats, save_file)
    return None

def load_game():
    """will be used to load a game"""
    data_chunk = []
    with open("saved_game.json", "r") as save_file:
        data_chunk = (json.load(save_file))
    return data_chunk