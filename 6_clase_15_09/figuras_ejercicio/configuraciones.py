import pygame
import math

pygame.init()#lo pongo aca para incializar la fuente que luego uso en otros modulos (si lo pongo en el principal no sirve)


#COLORES
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)
AZUL_CLARO = (0,150,255)
ROSA = (122,45,85)

#VENTANA Y FONDO
ancho = 500
alto = 500

PANTALLA = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('figuritas :p')

fondo = pygame.image.load("6_clase_15_09\matematicas.jpg")  
fondo = pygame.transform.scale(fondo, (ancho, alto))


fuente = pygame.font.SysFont("Arial", 20) #pygame.error: font not initialized
pi = math.pi




