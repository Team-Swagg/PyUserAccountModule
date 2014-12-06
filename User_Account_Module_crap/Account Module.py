#-----------------------------------------------------------------------
# User Account Module                                                  |
# by Sean Conrad                                                       |
#                                                                      |
# Summary:                                                             |
# Prompts user to create new account                                   |
# and writes account to a file, also allows                            |
# log in with an existing account                                      |
#-----------------------------------------------------------------------

import re

#Create new account-----------------------------------------------------
def newAccount():
	username = ''
	password = ''
	f = open('db.txt', 'r')           #Open database file
	contents = f.read()
	print 'Username and password must contain no spaces.'
	username = raw_input('Please type a new username. ')
	password = raw_input('Please type a new password. ')
	if re.search(r'[\s]', username):  #Checks for spaces in username.
		f.close()
		newAccount()
	elif re.search(r'[\s]', password):#Checks for spaces in password.
	    f.close()
	    newAccount()
	elif (username in contents):      #Checks for existing account name.
		print "Username already exists. Please try another username"
		f.close()
	else:
		f = open('db.txt', 'a')
		f.write(username  + ' ' + password)
		f.write('\n')
		f.close()
		print 'Account created'

#Log in with existing account-------------------------------------------
def existingAccount(name, passwrd):
	d = {}                            #Hold username and pass in a dict.
	with open("db.txt") as f:
		for line in f:
			(key, val) = line.split() #Checks exising accounts and adds to dict.
			d[str(key)] = val
	if name not in d:                 #Checks if username does not exists
		print 'Account name does not exist. '
	elif d[name] == passwrd:
		#This is where privileged account functions go.-----------------
		print 'Access Granted'
	else:
		print 'Access Denied'

#Question loop----------------------------------------------------------
while True:
	question = raw_input('New account? y/n ')
	if (question == 'y'):
		newAccount()

	elif (question =='n'):
		username = raw_input('Username: ')
		password = raw_input('Password: ')
		existingAccount(username, password)

	elif(question == 'quit'):
		exit()