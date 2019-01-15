# Quick test of RA8875 with Feather M4 Express
import time
import random
import busio
import digitalio
import board

import adafruit_ra8875 as ra8875
from adafruit_ra8875 import color565

# Configuration for CS and RST pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.D9)
rst_pin = digitalio.DigitalInOut(board.D10)
#int_pin = digitalio.DigitalInOut(board.D11)

# Config for display baudrate (default max is 12mhz):
BAUDRATE = 12000000

# Setup SPI bus using hardware SPI:
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Create the RA8875 display:
display = ra8875.RA8875(spi, cs=cs_pin, rst=rst_pin, baudrate=BAUDRATE)

# Main loop:
while True:
    # Fill the screen red, green, blue, then black:
    #for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    display.fill(color565((255, 0, 0)))
# Clear the display
#display.fill(0)
# Draw a red pixel in the center.
#display.pixel(display.width//2, display.height//2, color565(255, 0, 0))
# Pause 2 seconds.
#time.sleep(2)
# Clear the screen a random color
#display.fill(color565(random.randint(0, 255),
#                      random.randint(0, 255),
#                      random.randint(0, 255)))
# Pause 2 seconds.
#time.sleep(2)