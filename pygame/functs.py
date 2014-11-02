#Game functions and dictionaries
#-------------------------------

import time
import sys
import collections
import random

#DICTIONARIES!!----------------------------------------------------------------

# gameWeapons[player['weapon']]
gameWeapons = {
	'knife' :(0,1,2), 
	None	:(0,1), 
	'sword' :(0,1,2,3,4), 
	'hammer':(0,5,6,7,8),
	'axe'	:(0,4,5,6,7), 
	'spear' :(0,7,8,9),
}


inventoryItemQuantities ={
	'key' 		   :(0),
	'mana potion'  :(0),
	'health potion':(0),
}

marketItemQuantities = {
	'key' 		   :(0),
	'mana potion'  :(0),
	'health potion':(0),
}



gameItems = {
	'health potion' :(5),
	'mana potion' 	:(5),
	'key' 			:(1),

}

marketItems = {
	'health potion' :(15),
	'mana potion'	:(15),
	'hammer'		:(150),
	'spear'			:(200),
	'axe'			:(50),
	'sword'			:(20),	
}

spell = {
	'flame'	:(0,3,4,5,6,7,8,9,10,11),
	'ice'	:(0,6,7,8,9,10,11,12)
}

player = {
 	'name'  :None,
 	'health':(10),
 	'mana'  :(2),
 	'weapon':None,
  	'magic' :None,
}

spider = {
	'name'  :'spider',
	'health':(10),
	'attack':(0,1,2,3,4),
	'gold'	:(50),
}

elephant = {
	'name'  :'elephant',
	'health':(20),
	'attack':(0,5,6,7,8,9,10),
	'gold'	:(100),
}

inventoryItems = {
}

inventoryWeapons = {
}

#Creates an ordered dictionary. Call with 'orderedInventoryWeapons.items()[0]'
orderedInventoryWeapons = collections.OrderedDict((inventoryWeapons.items()))

gold = 50

#FUNCTIONS!!--------------------------------------------------------------------

def getPlayerStats():
	#Gets player stats
	orderedPlayer = collections.OrderedDict((player.items())) #Creates ordered dict
	for k, v in orderedPlayer.iteritems(): 
		print k,"\t" + str(v) #Iterates through dict and creates string with format

def getWeaponStats():
	#Get weapon's stats
	for k, v in inventoryWeapons.iteritems(): 
		print k, "has a " + str(v) + " damage rating" #Iterates through dict and creates string with format

def slowText(word): #Add a paramater 'speed' to control speeds of different things
	#Makes the text type letter by letter slowly.
	for i in word:
		time.sleep(0.04) #switch to .04 when done testing
		sys.stdout.write(i)
	time.sleep(1)
	print "\t"

def help():
	print ("COMMANDS: pstats, wstats, gold, i for inventory, fight, market, sw weapons")

def checkInventory():
	#Creates string of items in inventory
    inventoryItemsString = ", ".join(inventoryItems) #creates string out of list
    inventoryWeaponsString = ", ".join(inventoryWeapons)
    print str(inventoryItemsString) + ", " + str(inventoryWeaponsString)
    while True:
	    ask = raw_input('Type an item name to get info on it or type \'no\' ')
	    if (ask in inventoryWeapons):
	    	print (ask + ' has a damage rating of ' + str(inventoryWeapons[ask]))
	    elif (ask in inventoryItems):
	    	print (ask + ' has a rating of ' + str(inventoryItems[ask]))
		ask2 = raw_input("Use item? Yes or No ")
		ask2 = ask2.lower()
		if (ask2 == 'yes'):
			useItem(ask)
	    elif (ask == 'no'):
	    	break

#USE OF ITEMS IN INVENTORY  	
def useItem(item): #FIX SO THAT PLAYER CANNOT HEAL PAST FULL HEALTH
	if (item in inventoryItems):
		if (item == 'health potion'):
			player['health'] = player['health'] + inventoryItems['health potion']
			print ("Health potion rejuvinated " + str(inventoryItems['health potion']) + " health")
			print (player['name'] + "'s health = " + str(player['health']))
			del inventoryItems['health potion']
		elif (item == 'mana potion'):
			player['mana'] = player['mana'] + inventoryItems['mana potion']
			print ("Mana potion rejuvinated " + str(inventoryItems['mana potion']) + " mana")
			print (player['name'] + "'s mana = " + str(player['mana']))
			del inventoryItems['mana potion']
		elif item == 'key':#UPDATE ME!!!!!!
			pass
	else:
		print ('That item is not in your inventory.')
		time.sleep(1)

def weaponReceived(weapon):
	#Adds weapon to inventory
	slowText('You received ' + weapon + '!')
	inventoryWeapons[weapon] = gameWeapons[weapon]
	player['weapon'] = weapon

def itemReceived(item):
	#Adds item to inventory
	slowText('You received ' + item + '!')
	inventoryItems[item] = gameItems[item]

def updateGold(value):
	#Updates gold.
	global gold
	gold = value + gold
	print ("You have " + str(gold) + " gold.")

def addMagicToPlayer(key, val):
	# how to call the function addMagicToPlayer('flame',spell['flame'])
	player['magic'] = key
	slowText("Current magic is " + key)

def switchWeapons():
	#Switch main hand weapon.
	print ('Which weapon would you like to switch with?')
	inventoryWeaponsString = ", ".join(inventoryWeapons)
	print inventoryWeaponsString
	ask = raw_input()
	if (ask in inventoryWeapons):
		player['weapon'] = ask
		print ('Main weapon is now ' + ask)
	else:
		print ("That weapon is not in your inventory.")

def block():
	pass

#COMBAT SYSTEM-----------------------------------------------------------------

def startCombat():
	combat(player['weapon'], spider)

def combat(weapon, enemy):
	global gold
	#Creates the combat system
	execute = True
	execute2 = True
	execute3 = True
	slowText("You've encountered a " + enemy['name'] + "!")

	#WIN/LOSE TEXTS
	player_win = "You have defeated the " + enemy['name'] + "!"
	enemy_win  = "You have been defeated"

	while execute == True:
		#Gets a random int from the weapon player has and enemy attack rating.
		player_damage = random.choice(gameWeapons[player['weapon']])
		enemy_damage  = random.choice(enemy['attack'])
		player_magicDamage = random.choice(spell[player['magic']])

		slowText(player['name'] + "'s " + "beginning health = " + str(player['health']))
		slowText(enemy['name'] + "'s " + "beginning health = " + str(enemy['health']))

		ask = raw_input('Attack, Magic, Block, or Flee? ')
		ask = ask.lower()

		#PLAYER ATTACK
		if (ask == "attack"):
			slowText(player['name'] + ' does ' + str(player_damage) + " damage")
			enemy['health']  = enemy['health'] - player_damage
			slowText(enemy['name'] + "'s health = " + str(enemy['health']) + " health" )
			
			#HEALTH CHECK ON PLAYER/ENEMY
			if player['health'] <= 0:
				print enemy_win
				break
			elif enemy['health'] <= 0:
				print player_win
				gold = gold + enemy['gold']
				slowText("You receive " + str(enemy['gold']) + " gold!")
				break

		#PLAYER MAGIC ATTACK

		elif (ask == "magic"):
			if (player['mana'] > 0):
				player['mana'] = player['mana'] -1
				slowText(player['name'] + "'s mana = " + str(player['mana']))
				if (player_magicDamage > 0 and player['magic']==('flame')):
					if (player_magicDamage >= 10):
						print "CRITICAL HIT!"
					slowText("The flame ingulfs the " + enemy["name"] + " and does " + str(player_magicDamage) + " damage!")
					
				elif(player_magicDamage == 0):
					slowText("The flame missed the enemy!")
					
				enemy['health'] = enemy['health'] - player_magicDamage #Figures damage done to enemy and prints it
				slowText(enemy['name'] + " has " + str(enemy['health']) + " health" )
				
				#HEALTH CHECK ON PLAYER/ENEMY
				if player['health'] <= 0:
					print enemy_win
					break
				elif enemy['health'] <= 0:
					print player_win
					gold = gold + enemy['gold']
					slowText("You receive " + str(enemy['gold']) + " gold!")
					break
			elif (player['mana'] == 0):
				print("Mana is too low")
				time.sleep(1)
				continue

		#ENEMY ATTACK
		if (enemy_damage == 0):
			slowText("The " + enemy['name'] + " missed!")
		else:
			slowText(enemy['name'] + " does " + str(enemy_damage) + " damage")
			player['health'] = player['health'] - enemy_damage
			slowText(player['name'] + "'s health = " + str(player['health']))

		#HEALTH CHECK ON PLAYER/ENEMY
		if player['health'] <= 0:
			print enemy_win
			break
		elif enemy['health'] <= 0:
			print player_win
			gold = gold + enemy['gold']
			slowText("You receive " + str(enemy['gold']) + " gold!")
			break

#Market------------------------------------------------------------------------
def market():
	global gold
	slowText("Welcome to the Salty Potatoe.")
	slowText("Here's a list of our items:")
	for k, v in marketItems.iteritems(): 
		print k,"\t" + str(v) #Iterates through dict and creates string with format

	while True:
		ask = raw_input ("Type an item you would like to buy or type 'leave'. ")

		if (ask == 'leave'):
			break

		#Not in stock
		elif (ask not in marketItems):
			print "That item is not in our stock"
			time.sleep(1)

		#Purchase item in stock
		elif (ask in marketItems and gold >= marketItems[ask]):
			slowText("You have purchased " + ask + " for " + str(marketItems[ask]) + " gold")
			gold  = gold - marketItems[ask]
			if (ask in gameItems):
				inventoryItems[ask] = gameItems[ask]
			elif (ask in gameWeapons):
				inventoryWeapons[ask] = gameWeapons[ask]
			del marketItems[ask]
			time.sleep(1)

		#Not enough gold
		elif (gold <= marketItems[ask]):
			print "You do not have enough gold for that item."
			time.sleep(1)

def exit():
	ask = raw_input("Are you sure you want to exit? ")
	if (ask == 'yes'):
		sys.exit()