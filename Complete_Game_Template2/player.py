from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Start game at the reception 
current_room = rooms["Reception"]

def set_current_room(room):
	current_room = room