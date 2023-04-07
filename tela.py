import pygame


#initia o módulo pygame
pygame.init()

#criando tela

LARGURA_TELA = 600
ALTURA_TELA = 600

TELA = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption("Ufo")


#importar imagem
nave_espacial_image = pygame.image.load(f'ufo.png')
nave_espacial = nave_espacial_image.get_rect()
nave_espacial.center = (LARGURA_TELA//2,ALTURA_TELA//2 - 50)

#importar fonte
fonte_sistema = pygame.font.SysFont("Calibri",63)
fonte_personalizada = pygame.font.Font("AlloyInk-nRLyO.ttf",32)

#texto
texto_personalizado =  fonte_personalizada.render("Ufo Game!", True, (255,255,255))
texto_personalizado_rect = texto_personalizado.get_rect()
texto_personalizado_rect.center = (LARGURA_TELA//2,ALTURA_TELA//2 + 50) 

#loop principal
running = True
while running:
    #escutando eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    #adicionar uma imagem da tela
    TELA.blit(nave_espacial_image,nave_espacial)
    TELA.blit(texto_personalizado,texto_personalizado_rect)
    #atualiza a tela
    pygame.display.update()

#fim do jogo
pygame.quit()