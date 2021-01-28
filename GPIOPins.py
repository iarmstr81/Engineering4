#GPIO Pins
#Written by Imogen Armstrong

variable = 0

gpio mode 0 out
gpio mode 2 out

while variable <= 10: #need it to run through 10 times
  gpio mode 0 1
  gpio mode 2 1
  sleep 1 
  gpio mode 0 0
  gpio mode 2 0
  sleep 1 
  variable = variable + 1
else:
  done

