# AlphaPi

These are Python scripts that are meant to be used with the Adafruit 2.23" Monochrome OLED Bonnet (https://learn.adafruit.com/adafruit-2-23-monochrome-oled-bonnet/overview) although scripts with "sharp" in the name are meant to work with the 400x240 Sharp Memory Display from Adafruit.

## alphapi.py
alphapi.py is a basic text-entry script built using the curses module. Updates the screen with characters typed. Inspired by the Alphasmart.

### game.py
game.py allows you to use pygame functions and event handling without using its display functions (you continue to use PIL for that). The main point is to be able to use pygame for key presses. Still requires an HDMI display to be plugged in.

### gamewodis.py
gamewodis.py is my attempt to get pygame input without a display plugged in (headless) but so far have been unsuccessful.

### photo.py 
photo.py displays an image that you add to the same directory as the script.

