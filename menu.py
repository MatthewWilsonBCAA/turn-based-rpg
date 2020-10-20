import json
import file_management
import helper
import time

menu_logo = """
/--   ---   /-\   |-\   |\    | |   /--   ---
|      |    | |   | |   | |   | |   |      |
\-\    |    ---   ---   | |   | |   \-\    |
  |    |    | |   |\    | |   | |     |    |
--/    |    | |   | \   |/    \_/   --/    |

| /   ---   | |   /-\   |\    /-\   ---   /--
|/     |    |\|   |     | |   | |   |||   |  
|      |    | |   |     | |   | |   |||   \-\ 
|\     |    |\|   | \   | |   | |   |||     |
| \   ---   | |   \_/   |/    \_/   |||   --/
"""
stats = []
effects_list = [
    "No Effect", 
    "Bladed Attack", 
    "Flame Attack", 
    "Ranged Attack"]

def main_menu ():
    """Not for much, execpt showing the logo, and allowing the player to load/save data"""
    global menu_logo
    global stats
    helper.colored_text(menu_logo, 3)
    print("Welcome! Please enter an option!")
    print("new - Start a new game (will overwrite previous save)")
    print("load - Attempt to load a save")
    print("exit - Exit the game")
    choice = input()
    choice = choice.lower()
    data_chunk = []
    while True:
        if choice == 'new':
            file_management.new_game(stats)
            data_chunk = file_management.load_game()
            break
        elif choice == 'load':
            data_chunk = file_management.load_game()
            break
        elif choice == 'exit':
            quit()
        print("Invalid input. Please enter in one of the following: ")
        print("new - Start a new game (will overwrite previous save)")
        print("load - Attempt to load a save")
        print("exit - Exit the game")
        choice = input()
        choice = choice.lower()
    return data_chunk

def show_stats(stats: list) -> None:
    """Simply for printing out the stats of the player"""
    print(f"{stats[0]}'s statistics/'")
    helper.colored_text(f"---/Health: {stats[1]} of {stats[2]}", 0)
    helper.colored_text(f"---/Strength: {stats[3]}", 1)
    helper.colored_text(f"---/Power: {stats[4]}", 4)
    helper.colored_text(f"---/Defense: {stats[5]}", 2)
    print(f"---/Accuracy: {stats[6]}")
    helper.colored_text(f"---/Speed: {stats[7]}", 3)

def show_items(items: list) -> None:
    """Simply for printing out the items of the player"""
    global effects_list
    print("Items:")
    for i in items:
        helper.colored_text(f"{i[0]}/", 1)
        temp_string = effects_list[i[1]]
        helper.colored_text(f"---/{temp_string}", 1)
        helper.colored_text(f"---/Intensity: {i[2]}", 1)
        helper.colored_text(f"---/{i[3]}", 1)