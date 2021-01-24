#Man Shaped Pinata
#Written by Imogen Armstrong

import random
words = [
    "kitten", "puppy", "bird", "code", "data", "python", "raspberry", "pie"
]
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

def Pinata(PinataState):  #this is the array of the hangman drawings
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
        print("---┐")
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
print("Lives: ")
print(lives)
while lives > 0:
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
    else:
        lives = lives - 1
        print("wrong!")
        Pinata(PinataState)
        PinataState = PinataState + 1
        
if winLose == True:
    print("Congratulations! You Win!")
else:
    print("Sorry, you lost!")

   

