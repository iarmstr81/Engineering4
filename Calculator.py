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

#prints the operator name, and the doMath result of that operator using the two user numbers
print("Sum:\t\t" + str(doMath(input1,input2,1)))
print("Difference:\t" + str(doMath(input1,input2,2)))
print("Prodcut:\t" + str(doMath(input1,input2,3)))
print("Quotient:\t" + str(doMath(input1,input2,4)))
print("Modulo:\t\t" + str(doMath(input1,input2,5)))
