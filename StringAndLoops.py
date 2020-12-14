#Strings and Loops
#Imogen Armstrong
a = input("Enter sentence Here: ").split() #ask user for input and splits it into a list with a space between the words
#print(a) #for checking if the split worked

for x in range(0, len(a)): #a loop that runs for length of the string 
  for y in range(0,len(a[x])): #loop the runs for length
    print(a[x][y]) #prints a letter from the string
  print("-") # print a dash in between the words

