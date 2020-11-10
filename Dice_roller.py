#Automatic Dice Roller
#Written by Imogen A

from random import randint
import time
import sys

min = 1
max = 6

print ("Automatic Dice Roller")

while True:
	time.sleep(1)
	RollPrompt = input("Press ENTER to Roll or X to quit: ")

	if RollPrompt == (""):
		print(randint(min,max))
	if RollPrompt == ("x"):
		sys.exit()

