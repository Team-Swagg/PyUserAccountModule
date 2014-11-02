#------------------------
#Sean's Python text game|
#------------------------


#NOTES\\\\\\\
# Reset enemies health after fighting
# Add Penalty for losing
# Randomize enemies
# ADD MOVEMENT!!!!!!!!!!!!
# Add quantities to market and inventory for items
# Show weapon attack rating in 'stats'

#Imports
import functs
import time
import pygame

#Variables
name = ""
gameOn = True

#INTRO-------------------------------------------------------------------------

#Start music
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("data/music/lo-fi-world.wav")
pygame.mixer.music.queue("data/music/ox10c2.wav")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.1)


def begin():
	functs.slowText('You start to gain conciousness and open your eyes.')
	functs.slowText('It\'s dark out and you have a massive headache.')
	functs.slowText('As you roll over you almost fall into a river.')
	functs.slowText('''Struggling to stand and see that you are not far 
from your home and stagger to it.''')
	functs.slowText('''Upon grabbing the door handle, a man grabs your 
shoulder and shouts "Who are you!?"''')
	name = raw_input()
	functs.slowText('Here, ' + name + ' take this, you\'ll be needing it')
	functs.player['name'] = name

	functs.weaponReceived("knife")
	functs.itemReceived("health potion")
	functs.addMagicToPlayer('flame',functs.spell['flame'])

	functs.slowText('Type help to view commands')

	gameLoop()

#MAIN LOOP---------------------------------------------------------------------

def gameLoop():
	while (gameOn == True):
		question = raw_input("What would you like to do? ")
		if (question == "i"):
			functs.checkInventory()
		elif(question == "gold"):
			functs.updateGold(0)
		elif(question == "wstats"):
			functs.getWeaponStats()
		elif(question == "fight"):
			functs.startCombat()
		elif(question == "pstats"):
			functs.getPlayerStats()
		elif(question == "market"):
			functs.market()
		elif(question == "sw weapons"):
			functs.switchWeapons()
		elif(question == "help"):
			functs.help()
		elif(question == "name"):
			functs.slowText("Your name is " + functs.player['name'] + '.')
		elif(question == "exit"):
			functs.exit()
		elif(question in functs.inventoryItems):
			functs.useItem(question)



#Start of program!
begin()
