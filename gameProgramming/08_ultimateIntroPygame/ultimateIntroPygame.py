import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.time.Front('font/Pixeltype.ttf', 50)



sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('My game', False, 'Black')

player_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_surf = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION: 
        #   if player_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300)) 
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect, 10)
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(small_surf, snail_rect)
    screen.blit(player_surf,player_rect)


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #   print('jump')

    #if player_rect.colliderect(snail_rect):
    #    print('collision')

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)