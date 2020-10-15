import json
import file_management

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

def main_menu ():
    """Not for much, execpt showing the logo, and allowing the player to load/save data"""
    global menu_logo
    print(menu_logo)
    print("Welcome! Please enter an option!")
    print("new - Start a new game (will overwrite previous save)")
    print("load - Attempt to load a save")
    print("exit - Exit the game")
    choice = input()
    choice = choice.lower()
    while True:
        if choice == 'new':
            file_management.new_game()
            break
        elif choice == 'load':
            file_management.load_game()
            break
        elif choice == 'exit':
            quit()
        print("Invalid input. Please enter in one of the following: ")
        print("new - Start a new game (will overwrite previous save)")
        print("load - Attempt to load a save")
        print("exit - Exit the game")
        choice = input()
        choice = choice.lower()