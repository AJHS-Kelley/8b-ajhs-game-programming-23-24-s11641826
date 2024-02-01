import pygame
from sys import exit

player_rect = ()
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.time.Front('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect()

snail_surf = pygame.iamge.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_surf = player_surf.get_react(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:    
            #if player_rect.collidepoint(event.pos): print('collion')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surf,(300,50))

    snail_x_pos -= 4
    if snail_x_pos <= 0: snail_x_pos = 800
    screen.blit(snail_surf,(snail_x_pos,250))
    screen.blit(player_surf,player_surf)

    #if player_rect.colliderect(snail_rect):
    #    print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)