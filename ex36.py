from sys import exit

def dungeon_ooze():
	print "There is an ooze here."
	print "It has a sword inside"
	sword = False
	next = raw_input("fight or flee? >")

	if "fight"in next :
		for x in xrange(1,10):
			print "You attack, attack, attack ...."
			pass
		print "The ooze dies and you retrieve the sword"
		sword = True
	else:
		print "You escape safely... coward"
	pass
	return sword

def dungeon_mirror():
	print "There is a mirror on the back. What do you do?"
	shield = False;
	next = raw_input("> ")
	if ("look" in next):
		print "The mirror breaks, so your mind does. Game over"
		exit(0)
	else:
		print "That was clearly a deadly trap. You find a shield on your way out"
		shield = True
	pass

	return shield


def dungeon_maze():
	print "You start walking inside the maze"
	for x in xrange(1,50):
		print "Walk, turn left, turn left, left, right, straight"
		pass
	print "You finally made it out, empy-handed"
	pass

def dungeon_dragon():
	print "You found a brown dragon in this room"
	print "Would you play chess with him?"
	next = raw_input("> ")
	if "yes" in next:
		move = raw_input("Your next move?> ")
		if "knight"in move:
			print "Check mate!"
		elif "tower":
			print "Draw"
		else :
			print "You lose"
			pass
	print "You are such a sport. Congrats the dragon helps you out"
	pass

def start():
	print "4 doors ahead numbered 1 to 4"
	door_s = raw_input("your choice: ")
	door = int(door_s)

	if door == 1:
		if (dungeon_ooze()):
			print "You got a sword. The end"
	elif door == 2:
		if (dungeon_mirror()):
			print "You got a shield. The end"
	elif door == 3:
		dungeon_maze()
	elif door == 4:
		dungeon_dragon()		
	else:
		start()
	exit(0)
	pass

start()