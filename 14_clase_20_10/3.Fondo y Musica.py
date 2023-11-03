import pygame, pygame.locals

import sys

pygame.init()

SIZE = (1000,500)
PANTALLA = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mi juego")

icono = pygame.image.load("14_clase\Recursos\icono_homero.png")
pygame.display.set_icon(icono)


#FONDO
fondo = pygame.image.load("14_clase\\Recursos\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, SIZE)

#MUSICA DE FONDO
pygame.mixer.music.load("14_clase\Recursos\intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

PANTALLA.blit(fondo, (0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()