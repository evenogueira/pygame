import pygame
from pygame.locals import *

pygame.init()

altura = 400
largura = 400

x = 400/2
y = 400/2

tela = pygame.display.set_mode((altura,largura))

pygame.display.set_caption("Jogo da Eve")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0)) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.guit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                y -= 10
            elif event.key == K_DOWN:
                y += 10
            elif event.key == K_LEFT:
                x -= 10 
            elif event.key == K_RIGHT:
                x += 10

    pygame.draw.circle(tela,(255,0,0),(x,y),40)

    
    
    pygame.display.update()