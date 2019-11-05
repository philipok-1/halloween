#!/usr/bin/python3

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random

from gpiozero import MotionSensor

import subprocess

import os
import random

#print choose_file()

pir = MotionSensor(17)

pixel_pin = board.D12

num_pixels = 2

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.6, auto_write=False,
                           pixel_order=ORDER)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def choose_file():

    path ='/home/pi/scripts/halloween/sounds/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))

    return files[index]


def clear_pixels():

    pixels.fill((0,0,0))
    pixels.show()

def flash_pixels(times=15, colour=0, interval=.4):

    clear_pixels()
    for _ in range (times+1):

        colour_pixels(colour)
        
        time.sleep(interval)
        clear_pixels()
        time.sleep(interval)

def colour_pixels(colour):

    pixels.fill(wheel(colour))
    pixels.show()

def caught():

    global risk_level

    subprocess.call(["aplay", "/home/pi/scripts/halloween/sounds/415944__starblazer64__witchlaughter-1.wav"])
    flash_pixels()
    time.sleep(2)
    risk_level=0
    clear_pixels()

#subprocess.Popen(["aplay", "/home/pi/scripts/halloween/sounds/487653__nicknamelarry__happy-halloween-evil-voice.wav"])

#START ROUTINE

#clear_pixels()
#flash_pixels()
#time.sleep(1)

#colour_pixels(250)
#subprocess.Popen(["aplay", "/home/pi/scripts/halloween/sounds/473615__wangzhuokun__ghostly-ambient-voice.wav"])
#time.sleep(40)


#SET UP MOTION SENSOR

clear_pixels()

while True:

    colour=int(input("colour: "))
    colour_pixels(colour)
    time.sleep(2)
    clear_pixels()
