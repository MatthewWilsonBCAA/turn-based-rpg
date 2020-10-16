#this file simply stores all helper functions, none in which have a specific place
import os
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear')
def represents_int(s):
    """Returns true if it is an integer, returns false if it is not"""
    try: 
        int(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

def colored_text(line: str, color: int):
    """This function allows the printing out of different colored text
    0 is for red, 1 is for cyan, 2 is for green, 3 is for yellow, 4 is for purple"""
    if color == 0:
        print("\033[91m{}\033[00m".format(line))
    elif color == 1:
        print("\033[96m{}\033[00m".format(line))
    elif color == 2:
        print("\033[92m{}\033[00m".format(line))
    elif color == 3:
        print("\033[93m{}\033[00m".format(line))
    elif color == 4:
        print("\033[95m{}\033[00m".format(line))
    elif color == 5:
        print("\033[31m{}\033[00m".format(line))