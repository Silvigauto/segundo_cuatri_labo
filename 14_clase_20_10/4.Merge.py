import pygame
from ClassImagen2 import Imagen

pygame.init()

#COLORES
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)
AZUL_CLARO = (0,150,255)
ROSA = (122,45,85)


velocidad = 10
ANCHO = 1000
ALTO = 500


PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi juego")

#ICONO
icono = pygame.image.load("14_clase\Recursos\icono_homero.png")
pygame.display.set_icon(icono)


#FONDO
fondo = pygame.image.load("14_clase\Recursos\\fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

#MUSICA DE FONDO
pygame.mixer.music.load("14_clase\Recursos\intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


#IMAGEN VERTICAL
imagen_vertical = Imagen((ANCHO//2, ALTO//2), (80,80), "14_clase\Recursos\dona.png")


#IMAGEN HORIZONTAL
imagen_horizontal = Imagen((ANCHO-100, ALTO//2), (100,150), "14_clase\Recursos\homero.png")

PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("mi juego")

clock = pygame.time.Clock()
FPS = 30

bandera = True
while bandera:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
    
    PANTALLA.blit(fondo, (0,0))

    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)


    #imagen_vertical.detectar_colision(imagen_horizontal)
    #MOVE
    imagen_vertical.mover('Vertical', velocidad, PANTALLA)
    imagen_horizontal.mover('Horizontal', velocidad, PANTALLA)

    pygame.display.update()

pygame.quit()
