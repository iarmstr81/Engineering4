import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
leds = [38] #  put the physical pin number here
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT) # sets the pins to output

for i in range(0, 3): # blinks the LED(s) 3 times
	GPIO.output(leds, 1)
	time.sleep(0.5)
	GPIO.output(leds, 0)
	time.sleep(0.5)
	print("hi")
