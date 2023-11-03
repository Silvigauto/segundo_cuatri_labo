import pygame
import sys
from pygame.locals import *
from configuraciones import *

def mover_personaje(rectangulo, velocidad, pantalla):
    x_nueva = rectangulo.x + velocidad
    if x_nueva < pantalla.get_width() and x_nueva > 0:
        rectangulo.x += velocidad

def animar_personaje(pantalla, lista_imagenes, rectangulo_personaje, contador_pasos):
    largo = len(lista_imagenes)
    if contador_pasos >= largo:
        contador_pasos = 0
    
    pantalla.blit(lista_imagenes[contador_pasos], rectangulo_personaje)

    contador_pasos += 1
    return contador_pasos




def actualizar_pantalla(pantalla, fondo, que_hace, acciones, rectangulo_personaje, contador_pasos):    
    pantalla.blit(fondo, (0,0))

    match que_hace:
        case "Quieto":
            animar_personaje(pantalla, acciones["Quieto"], rectangulo_personaje, contador_pasos)
        case "Derecha":
            animar_personaje(pantalla, acciones["Derecha"], rectangulo_personaje, contador_pasos)
            mover_personaje(rectangulo_personaje, 10, pantalla)
    
    return contador_pasos

W,H = 1900,900
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))

#FONDO
fondo = pygame.image.load("16_clase_27_10_ger\corre\\fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (W,H))

#personaje

contador_pasos = 0

acciones = {}
acciones["Quieto"] = personaje_quieto
acciones["Derecha"] = personaje_camina_derecha

reescalar_imagenes(acciones, 100,90)

x_inicial = H//2 - 400
y_inicial = 760
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

que_hace = "Quieto"

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        que_hace = "Derecha"
    else:
        que_hace = "Quieto"

    contador = actualizar_pantalla(PANTALLA, fondo, que_hace, acciones, rectangulo_personaje, contador_pasos)
    pygame.display.update()

pygame.quit()
sys.exit()