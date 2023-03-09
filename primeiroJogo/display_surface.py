import pygame
from pygame.locals import *

pygame.init()

altura = 300
largura = 300

x = 40
y = 0

tela = pygame.display.set_mode((altura,largura))

pygame.display.set_caption("Jogo da Eve")


while True:
    tela.fill((0,0,0)) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.guit()
            exit()
    pygame.draw.circle(tela,(255,0,0),(x,y),40)

    if y > altura:
        y=0
    y = y+1

    pygame.time.delay(10)
    pygame.display.update()