# Final Project, Albert Laguerre, v0.0
import sys, random, pygame

resolution = 0  # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for EASY or 2 for HARD!"))

pygame.display.set_caption('NAME OF GAME -- EASY')
pygame.display.set_caption('NAME OF GAME -- HARD')

if difficulty == 1:
    pygame.display.set_caption('NAME OF GAME -- EASY')
else:
    pygame.display.set_caption('NAME OF GAME -- HARD')
screen = pygame.desplay.set_mode((x, y))
# CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080


