import pygame
from helper import *

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
gameClock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("World Generation")

player=Player(screen,100,100,10,10,0.5)

run=True
while run:
    deltaTime = gameClock.tick()
    print(deltaTime)
    
    key=pygame.key.get_pressed()
    player.update(key,deltaTime)

    # if key[pygame.K_LEFT]:
    #     player.move_ip(-1*deltaTime,0)
    # if key[pygame.K_RIGHT]:
    #     player.move_ip(deltaTime,0)
    # if key[pygame.K_UP]:
    #     player.move_ip(0,-1*deltaTime)
    # if key[pygame.K_DOWN]:
    #     player.move_ip(0,deltaTime) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    pygame.display.update()
pygame.quit()
