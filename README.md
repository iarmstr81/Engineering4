# Engineering4
My Engineering 4 work

# Table of Contents
* [Pi Online](#Pi-Online)
* [Hello Python/Dice Roller](#Hello-Python/Dice-Roller)
* [Program 01 Calculator](#Program-01-Calculator)
* [Program 02 Quadratic Solver](#Program-02-Quadratic-Solver)
* [Program 03 Strings and Loops](#Program-03-Strings-and-Loops)
* [Challenge Man Shaped Piñata](#Challenge-Man-Shaped-Piñata)

## Pi Online
In this assignment I was tasked with connecting my raspberry pi to the internet. My pi wouldn't connect to the wifi at my house but I did manage to connect it to my personal hotspot. I had to take the space out of the name of my phone and it took a few tries before it actually connected. I couldn't find any reason for it to not be connecting so I just kept trying and eventually it connected. I would love to be able to connect it to my home wifi because it would make it so much easier to push to my repo. This is because everytime I forget that I have to turn on my hotspot before trying to push anything to my repo.

## Hello Python/Dice Roller
### Description
This assignment is from the Hello Python module. In this assignment we had to create a python file that would roll a die when enter was pressed and when x was pressed the program would quit.
### Code
```python
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
```
### Images
<img src="Pictures/DiceRollerPicture.png" width="400">

### Reflection
I struggled with this assignment in the beginning because I didn't know how I would be able to press enter and get feedback. However after I figured it out it out the rest of the code was easy.

## Program 01 Calculator
### Description
In this module, we had to make a calculator in python. We had to have the user input 2 numbers, then run those numbers through one function, and recieve the results of the 5 different operators (Addition, Subtraction, Multiplication, Division, Modulo)
### Code
```python
##Caluclator
##Imogen Armstrong

input1 = input("Select First Number: ") 
input2 = input("Select Second Number: ")

def doMath(input1,input2,operator):
        #Do Math Function, takes the 2 numbers, and decides which operator to use, and returns the value
        if operator == 1: #sum
                return int(input1) + int(input2) 
        
        if operator == 2: #difference
                return int(input1) - int(input2)
        if operator == 3: #product
                return int(input1) * int(input2)
        if operator == 4: #quotient
                Q = int(input1) / int(input2) #finds quotient
                RQ = round(Q,2) #rounds quotient to 2 places
                return RQ
        if operator == 5: #modulus
                return int(input1) % int(input2)

#prints the operator name, and the doMath result of that operator using the two$
print("Sum:\t\t" + str(doMath(input1,input2,1)))
print("Difference:\t" + str(doMath(input1,input2,2)))
print("Prodcut:\t" + str(doMath(input1,input2,3)))
print("Quotient:\t" + str(doMath(input1,input2,4)))
print("Modulo:\t\t" + str(doMath(input1,input2,5)))
```
### Images
<img src="Pictures/CalculatorPicture.png" width="300">

### Reflection
This assignment really helped reteach/remind me how to use functions with parameters. Basically when you define the function you need to declare that the function will need parameters. It will then use those parameters when you call the function to get a result.

## Program 02 Quadratic Solver
### Description
In this assignment we had to make a quadratic solver. So, the user will input values for a, b, & c to fill out the quadratic formula. The program then produces the roots if there are roots. If it does not have roots it will produce that it does not have any roots.
### Code
```python
#Written by Imogen Armstrong
#Quadratic Solver
print("Quadratic Solver")
print("Enter the coefficients for ax^2+bx+c:")
input1 = input("Select a: ")
input2 = input("Select b: ")
input3 = input("Select c: ")

inputArray = [int(input1), int(input2), int(input3)]
rootArray = []

def discrimFunc(vals):
    a = vals[0]
    b = vals[1]
    c = vals[2]
    if b * b - 4 * a * c < 0:
        rootArray.append("No Real Roots")
    else:
        rootA = (-b+(b*b-4*a*c)**(1/2))/(2*a)
        rootB = (-b-(b*b-4*a*c)**(1/2))/(2*a)
        #rounds the roots to 2 places
        RrootA = round(rootA, 2)
        RrootB = round(rootB, 2)
        #adds final roots to the rootArray
        rootArray.append(RrootA)
        rootArray.append(RrootB)

        return rootArray

print(discrimFunc(inputArray))
if len(rootArray) == 2:
  print(str(rootArray[0]) + " " + str(rootArray[1]))
else:
   print(rootArray)
```
### Images
<img src="Pictures/QuadraticSolver.png" width="300">

### Reflection
This code took me awhile because I ran into an error. Everything that should of fixed it wouldn't. Until one day I did something I don't remember what it was but then it worked. Except for that issue I did really enjoy this assignment. It was really good to get practice using arrays. 

## Program 03 Strings and Loops
### Description
In this assignment, we had to create a program that would take a input sentence and print it out letter by letter with a dash(-) in place of each space.
### Code
```python
#Strings and Loops
#Imogen Armstrong
a = input("Enter sentence Here: ").split() #ask user for input and splits it into a list with a space between the words
#print(a) #for checking if the split worked

for x in range(0, len(a)): #a loop that runs for length of the string 
  for y in range(0,len(a[x])): #loop that runs for length
    print(a[x][y]) #prints a letter from the string
  print("-") # print a dash in between the words
```
### Images
<img src="Pictures/StringsandLoops.png" width="300">

### Reflection
I went into thinking this assignment would be a lot harder than it was because it seemed so complicated having to print out each individual letter. 

## Challenge Man Shaped Piñata
### Description
In this assignment we were tasked with recreating the classic game Hangman or as we call it Man Shaped Piñata. I turned it from a two player game to a single player game. The program starts by picking a word from a list and then asks you to guess a letter.
### Code
```python
#Man Shaped Pinata
#Written by Imogen Armstrong

import random
words = ["kitten", "puppy", "bird", "code", "data", "python", "raspberry", "pie"] #list of words the program chooses from
answer = words[random.randint(0, len(words) - 1)]
#print(answer) #for testing
alist = []
lives = 6
letterInput = " "
rightGuess = 0  #amount of correct guesses
winLose = None  #set to true or false, triggers an end game messege
PinataState = 0  #state of the drawing
uniqueChar = len(set(answer))  #finds amount of unique characters

for x in range(len(answer)):  #makes array as long as the answer
    alist.extend('_')

def Pinata(PinataState):  #this is the array of the man pinata drawings
  if PinataState == 0:
        print(" ")
        print("---|")
        print(" ")
  if PinataState == 1:
        print(" ")
        print("---|")
        print("   0")
        print(" ")
  if PinataState == 2:
        print(" ")
        print("---|")
        print("   0")
        print("  / ")
        print(" ")
  if PinataState == 3:
        print(" ")
        print("---|")
        print("   0")
        print("  /|")
        print(" ")
  if PinataState == 4:
        print(" ")
        print("---|")
        print("   0")
        print("  /|\ ")
        print(" ")
  if PinataState == 5:
        print(" ")
        print("---|")
        print("   0")
        print("  /|\ ")
        print("  /  ")
        print(" ")
  if PinataState == 6:
        print(" ")
        print("---|")
        print("   0")
        print("  /|\ ")
        print("  / \ ")
        print(" ")

print("Welcome to Man-Shaped Pinata!")
print("Lives: ") #shows you yor number of lives
print(lives)
while lives > 0: #if you still have lives asks for another guess
    letterInput = input("Enter your guess: ")
    if letterInput in answer:
        print("Correct!")
        for x in range(len(answer)):
            if letterInput == answer[x]:
                alist[x] = letterInput
        print(alist)
        rightGuess = rightGuess + 1
        Pinata(PinataState)

        if rightGuess == uniqueChar:
            winLose = True
            break
    else: #if you wrong subtracts a life and prints man
        lives = lives - 1
        print("wrong!")
        Pinata(PinataState)
        PinataState = PinataState + 1
        
if winLose == True:
    print("Congratulations! You Win!")
else:
    print("Sorry, you lost!")
```
### Images
<img src="Pictures/MSPPicture.png" width="300">

### Reflection
This code took me awhile to figure out because I wasn't sure how I was going to do it. I started by setting up the list of words and getting it to pick a random one. After I had that I moved on to setting up how the man shaped piñata would print. I then figured out how the guessing would work.

<<<<<<< HEAD
## GPIO pins - Bash
### Discription
In this assignment, we had to make an LED blink 10 times using bash.
### Code
```python
gpio -g mode 1 out
gpio -g mode 2 out
num=0 

while[ $num -le 19]
do
        /usr/bin/gpio -g toggle 1
	/usr/bin/gpio -g toggle 2
        sleep .5
	let "num += 1"
	echo"$num"
done
gpio -g write 1 0 
gpio -g write 2 0 
```
### Images

### Reflection

This module was a bit tricker than previous ones. It took me a little bit of research but eventually I figured it out.

## GPIO Pins I2C
### Description
In this assignment we were tasked with using an accelerometer and an OLCD screen. I used the values I recieved from the accelerometer and then showed those values on the screen. A lot of this assignment was downloading and learning how to use the screen and accelerometer.

### Code
```
import time
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303() #accelerometer setup
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_address=0x3d)#display setup
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()


while True:
	accel, mag = accelerometer.read() # gets accelerometer data
	accel_x, accel_y, accel_z = accel #sets the acceleration values
	mag_x, mag_y, mag_z = mag #although I don't use this, the .read() takes 6 points of data, so you need to give places for all 6 data points
	
  #(0,0) is the top left corner and adding to each value moves it right or left
	draw.text((x, top), "Accelerometer Data:", font=font, fill=255)
	draw.text((x, top + 10), "Accel x ={0}".format(round(accel_x / 100, 3)), font=font, fill=255) # draws x 
	draw.text((x, top + 20), "Accel y ={0}".format(round(accel_y / 100, 3)), font=font, fill=255) # draws y
	draw.text((x, top + 30), "Accel z ={0}".format(round(accel_z / 100, 3)), font=font, fill=255) # draws z

	disp.image(image)
	disp.display()

  #clears screen so values can be updated
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0) # "refreshes" the xyz values so they can be updated
	disp.image(image)
	disp.display()

	#added a sleep just for fun and to make sure nothing dies
	time.sleep(.1)
```

### Images
<img src="Pictures/I2Cwiring.jpg" width="300">

### Reflection
This code took a bit off troubleshooting with what parts of code were actually needed to use both the accelerometer and screen. The code from the two examples we ran after downloading to test were very helpful especially since a lot of the lines of code come from it. I link the githubs so they are easier to look at. I was having some trouble with getting the values to show on the screen so I refrenced classmates and Graham's was very helpful. 

[OLED Screen](https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py)

[Accelerometer](https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/examples/simpletest.py)

>>>>>>> d2593e954a05fa469252217f15760cf32f74b9e7
