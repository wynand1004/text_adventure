# Text Adventure Demo
# Inspired by classic Infocom text adventures
import os
os.system("clear")
import time

# Game class
class Game(object):
	def __init__(self):
		self.state = "start"
		self.message = ""
		self.items = []
		self.rooms = []
		
	def print_header(self):
		print("""
     _       _                 _                  
    / \\   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
   / _ \\ / _` \\ \\ / / _ \\ '_ \\| __| | | | '__/ _ \\
  / ___ \\ (_| |\\ V /  __/ | | | |_| |_| | | |  __/
 /_/   \\_\\__,_| \\_/ \\___|_| |_|\\__|\\__,_|_|  \\___|\n\n""")
		
	def print_exits(self, location):
	
		exits = ""
		for key in location.exits:
			exits += key + " "
		
		print("\nHere are the exits: {}\n".format(exits))	
			
		
	def	print_location(self, location):
		print("""
You are {}.\n\n{}\n""".format(location.short_description, location.description))

	def print_items(self, location):
		print("You can see the following items: ")
		for item in location.items:
			print(item.short_name)
		print("\n")
		
	def press_enter_to_continue(self):
		delay = input("\nPress enter to continue. > ")
		
	def set_message(self, message):
		self.message = message	
	
	def print_message(self):
		print(self.message)
		print()
		self.message = ""
				

# Player Class
class Player(object):
	def __init__(self, location):
		self.location = location
		self.health = 100
		self.inventory = []
		self.description = "You are are a tremendously average person. Average height\
							average weight, and average looks"
							
	def print_health(self):
		print("\nPlayer Health: {}".format(self.health))
		
	def print_inventory(self):
		print("You have:")
		for item in player.inventory:
			print(item.short_name)
		print()
		game.press_enter_to_continue()	
	
	def move(self, direction):
		if (direction == "N") and ("N" in player.location.exits):
			player.location = player.location.exits["N"]
		elif (direction == "S") and ("S" in player.location.exits):
			player.location = player.location.exits["S"]
		elif (direction == "E") and ("E" in player.location.exits):
			player.location = player.location.exits["E"]
		elif (direction == "W") and ("W" in player.location.exits):
			player.location = player.location.exits["W"]
		elif (direction == "U") and ("U" in player.location.exits):
			player.location = player.location.exits["U"]
		elif (direction == "D") and ("D" in player.location.exits):
			player.location = player.location.exits["D"]
		else:
			print("Sorry, you cannot go that way.")
			time.sleep(2)
	
	def has(self, short_name):
		for item in self.inventory:
			if item.short_name == short_name:
				return True
		else:
			return False
						
#Room class
class Room(object):
	def __init__(self, short_description = None, description = None, exits = {}):
		self.short_description = short_description
		self.description = description
		self.exits = {}
		for exit in exits:
			self.exits[exit] = exits[exit]
			
		self.items = []
		game.rooms.append(self)
			
	def initialize(self, short_description = None, description = None, exits = {}):
		self.short_description = short_description
		self.description = description
		self.exits = {}
		for exit in exits:
			self.exits[exit] = exits[exit]

	def has(self, short_name):
		for item in self.items:
			if item.short_name == short_name:
				return True
		else:
			return False

	def enter(self):
		pass
		
	def process_command(self, noun, verb):
		pass
		
	def exit(self):
		pass

# Item class						
class Item(object):
	def __init__(self, short_name = None, description = None, location =  None):
		self.short_name = short_name
		self.description = description
		location.items.append(self)
		self.state = "active"
		game.items.append(self)
		
	def get(self):
		pass
		
	def drop(self):
		pass
	
game = Game()

# Create rooms
front_door = Room()
front_of_house = Room()

front_door.initialize("in front of a door", "The door is connected to a house. It is an old door with a knocker on it.", {"N": front_of_house})
front_of_house.initialize("in front of a house", "It is an old and run down house.", {"S": front_door})

# Create items
note = Item("NOTE", "The note reads: Welcome to Adventure! You need to find the sword of destiny in the Tower of Fear.", front_of_house)

player = Player(front_of_house)

while True:	
	game.print_header()
	
	game.print_message()
	
	game.print_location(player.location)
	
	game.print_exits(player.location)
	
	game.print_items(player.location)
	
	player.print_health()
	
	command = input("\nWhat would you like to do? > ").upper()
	
	# Single word commands
	if command in ["INV", "INVENTORY"]:
		player.print_inventory()
		
	# Move (single letters)
	elif command in "NSEWUD":	
		player.move(command)
		continue
		
	# Multi word commands		
	words = command.split(" ")
	if len(words) > 0:
		verb = words[0].strip()
	
	if len(words) > 1:
		object = words[1].strip()
	
	# Get item
	if verb in ["GET", "TAKE", "GRAB", "STEAL"]:
		# Check if the item is in the current location
		for item in player.location.items:
			if item.short_name == object:
				game.set_message("You take the {}.".format(item.short_name))
				player.location.items.remove(item)
				player.inventory.append(item)
				break
		
	# Drop item
	if verb in ["DROP", "GIVE"]:
		# Check if the item is in the current location
		for item in player.inventory:
			if item.short_name == object:
				game.set_message("You drop the {}.".format(item.short_name))
				player.location.items.append(item)
				player.inventory.remove(item)	
				break	
		
	# Examine
	if verb in ["READ", "EXAMINE", "EXA"]:
		# Check if it is in the inventory
		for item in game.items:
			if item.short_name == object:
				game.set_message(item.description)
				break
		
		# Check if it is in the room
		for item in player.location.items:
			if item.short_name == object:
				game.set_message(item.description)
				break		
		
	
	
				
		