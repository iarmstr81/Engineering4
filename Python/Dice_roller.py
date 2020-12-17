#Automatic Dice Roller
#Written by Imogen A

from random import randint
import time
import sys

min = 1 #minimum number that you can get
max = 6 #maximum number that you can get

print ("Automatic Dice Roller") #Set up/title

while True:
	time.sleep(1) #delay so it doesn't get overwhelmed
	RollPrompt = input("Press ENTER to Roll or X to quit: ") #asking for input

	if RollPrompt == (""): #if enter is pressed
		print(randint(min,max)) #print a number between 1 and 6
	if RollPrompt == ("x"): #if x is pressed
		sys.exit() #ends the program

