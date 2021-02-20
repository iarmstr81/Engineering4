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
