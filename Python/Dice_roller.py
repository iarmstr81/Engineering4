# Automatic Dice Roller
# Written by Imogen A

import random
import keyboard
import time

min = 1
max = 6
active= True
print("Automatic Dice Roller")
print("press ENTER to roll")
print("press X to quit")

while active == True:
  if keyboard.is_pressed('enter'):
    print(random.randint(min, max))
    time.sleep(2)
