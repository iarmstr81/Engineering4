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
