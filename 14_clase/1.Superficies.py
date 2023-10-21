import pygame
from ClassImagen import Imagen
#COLORES
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)
AZUL_CLARO = (0,150,255)
ROSA = (122,45,85)

ANCHO = 800
ALTO = 600
velocidad = 10
FPS = 30

pygame.init()


#IMAGEN VERTICAL
imagen_vertical = Imagen((ANCHO//2, ALTO//2), (100,100), (VERDE,BLANCO))


#IMAGEN HORIZONTAL
imagen_horizontal = Imagen((ANCHO-100, ALTO//2), (100,100), (AZUL_CLARO,ROJO))


PANTALLA = pygame.display.set_mode((ANCHO,ALTO))

clock = pygame.time.Clock()

bandera = True
while bandera:
    clock.tick(FPS)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            bandera = False
    
    PANTALLA.fill(NEGRO)

    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)


    imagen_vertical.detectar_colision(imagen_horizontal)
    #MOVE
    imagen_vertical.mover('Vertical', velocidad, PANTALLA)
    imagen_horizontal.mover('Horizontal', velocidad, PANTALLA)

    pygame.draw.line(PANTALLA,AZUL, (ANCHO//2,0), (ANCHO//2,ANCHO), 1)
    pygame.draw.line(PANTALLA,AZUL, (0,ALTO//2), (ANCHO,ALTO//2), 1)

    pygame.display.update()

pygame.quit()
