# Fianl Project, Albert Laguerre, v0.0

import pygame
import random
import sys

pygame.init

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Easy Level")

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

snake_block = 20
snake_speed = 10

food_size = 20

font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

