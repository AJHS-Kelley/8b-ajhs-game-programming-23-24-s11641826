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

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

def draw_food(food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])

def easy_level():
    snake_list = []
    snake_length = 1 
    snake_x = screen_width // 2
    snake_y = screen_height // 2
    snake_x_change = 0
    snake_y_change = 0
    food_x = round(random.randrange(0, screen_width - food_size) / 20) * 20
    food_y = round(random.randrange(0, screen_height - food_size) / 20) * 20

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

