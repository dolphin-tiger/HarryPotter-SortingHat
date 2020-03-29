# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
#import digitalio
import RPi.GPIO as GPIO
import random

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 12

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixelOff = (0,0,0)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.7, auto_write=False, pixel_order=ORDER
)

#Button press setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
btn = GPIO.input(21)

## btn = digitalio.DigitalInOut(board.D21)
## btn.direction = digitalio.Direction.INPUT
## btn.pull = digitalio.Pull.UP
def btnPress(pin):
    for x in range(3):
        rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
        h = random.randint(0,3)
        houseName, c1, c2, saying = setHouse(h)
        #print(houseName)
    print(saying)
    displayHouse(c1, c2)

GPIO.add_event_detect(21, GPIO.RISING, callback=btnPress)


#Colors
#Griffindor
Scarlet  = (128,  0,  0)
Gold     = ( 64, 64,  8)
#Hufflepuff
Yellow   = (128, 64,  0)
Black    = (  0,  0,  0)
#Ravenclaw
Blue     = ( 16, 24,128)
Bronze   = ( 64, 32, 12)
#Slitherin
Green     = ( 10, 98, 23)
Silver    = ( 64, 64, 64)

# Houses array
house0 = {"name" : "Gryffindor", "color1" : Scarlet, "color2" : Gold   , "saying":"Then we better make you... GRYFFINDOR!"}
house1 = {"name" : "Hufflepuff", "color1" : Yellow , "color2" : Black  , "saying":"Yes, loyal, just, you belong with... HUFFLEPUFF!"}
house2 = {"name" : "Ravenclaw" , "color1" : Blue   , "color2" : Bronze , "saying":"Of wit and learning, RAVENCLAW it shall be!"}
house3 = {"name" : "Slytherin" , "color1" : Green  , "color2" : Silver , "saying":"hmmm... SLYTHERIN!"}

houses = {"house0" : house0, "house1" : house1, "house2" : house2, "house3" : house3}

def setHouse(house):
	s = "house" + str(house)
	h = houses.get(s).get("name")
	c1 = houses.get(s).get("color1")
	c2 = houses.get(s).get("color2")
	s = houses.get(s).get("saying")

	#print(s, h, str(l))
	return h, c1, c2, s

def oppositePixels(index):
    p1 = index % num_pixels
    p2 = (index + (num_pixels // 2)) % num_pixels
    return p1, p2

# color wheel    
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

#def color_chase(color, wait):
#    for i in range(num_pixels):
#        pixels[i] = color
#        time.sleep(wait)
#        pixels.show()
#    time.sleep(0.5)

def colorTwo_chase(color1, color2, loops, wait):
    for l in range(loops):
        for i in range(num_pixels):
            p1, p2 = oppositePixels(i)
            pixels[p1] = color1
            pixels[p2] = color2
            time.sleep(wait)
            pixels.show()
        #time.sleep(wait)
    time.sleep(0.5)

def colorTwo_alternating(color1, color2, loops, wait):
    for l in range(loops):
        for i in range(num_pixels):
            #p1, p2 = oppositePixels(i)
            if (i + (l % 2)) % 2 == 0:
                pixels[i] = color1
            else:
                pixels[i] = color2
            #time.sleep(wait)
        pixels.show()
        time.sleep(wait)
    time.sleep(0.5)


# rainbow color wheel effect
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def displayHouse(c1, c2):
    #pixels.fill(pixelOff)
    #pixels.show()

    time.sleep(0.5)
    colorTwo_chase(c1, c2, 5, 0.1)
    #colorTwo_alternating(c1, c2, 25, 0.5)
    colorTwo_chase(c1, c1, 1, 0.1)

    time.sleep(3)
    pixels.fill(pixelOff)
    pixels.show()

#startup indicator - run this to show the script is running
for x in range(5):
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
pixels.fill(pixelOff)
pixels.show()
iB = 0

while True:
    if GPIO.event_detected(21):
        print('Hmm... but where to put you?')
    time.sleep(0.1)

# this captures any button actions
#while True:
#    if btn.value == True and iB == 0:
#        iB = 1
#        for x in range(6):
#            rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
#            h = random.randint(0,3)
#            houseName, c1, c2 = setHouse(h)
#            print(houseName)
#        displayHouse(c1, c2)
#
#    elif btn.value == False and iB == 1:
#        iB = 0
#    time.sleep(0.1)