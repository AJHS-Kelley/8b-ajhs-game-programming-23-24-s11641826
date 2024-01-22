# Number Slider, by Albert Laguerre, based on a project by AI Sweigart, v0.0

import sys, random, pygame
# sys module provides access to system resources (i.e Operating system commands)

from pygame.locals import *
# Allows us to call funcations from pygame using just the funcation name instead of module.functions()
# Example: We can use draw() instead of pygame.draw()

# Constants for Game Board
BOARDWIDTH = 4 # COLUMS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30 # this is a maximum value! WONT MAKE A SLOW COMPUTER RUN FASTER
BLANK = None 

# COLOR VALUES IN (R, G, B) format.
# 0 = No Value, 255 = Max Value
Black = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# BOARD DESIGN SETUP
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BOREDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20