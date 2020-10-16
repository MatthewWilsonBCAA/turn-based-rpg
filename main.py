import random
import menu

data_chunk = menu.main_menu()
menu.show_stats(data_chunk[0])
if data_chunk[1]:
    menu.show_items(data_chunk[1])