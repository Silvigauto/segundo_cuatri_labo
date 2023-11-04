import pygame
from pygame.locals import *
from configuraciones import *
from Modo import *

pygame.init()

def crear_plataforma(visible,tamaño, x,y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma




W, H = 1300, 600
FPS = 18

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# Fondo
fondo = pygame.image.load("clase15(desarrollo)\\assets\\fondo.jpg")
fondo = pygame.transform.scale(fondo, (W, H))


x_inicial = H/2 - 400
y_inicial = 760



contador_pasos = 0

diccionario = {}
diccionario["Quieto"] = personaje_quieto
diccionario["Derecha"] = personaje_derecha
diccionario["Izquierda"] = personaje_izquierda
diccionario["Salta"] = personaje_salta


mario = Personaje(diccionario, (70,60), 0, 600,5 )

#PISO

#piso = pygame.Rect(0,550,W,20)
piso = crear_plataforma(False, (W,20), 0,663)

plataforma_caño = crear_plataforma(True, (100,100), 850, 550, "corre\Caño (2).png")
plataformas = [piso, plataforma_caño]


bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == KEYDOWN:
            if evento.key == K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        mario.que_hace = "Derecha"
    elif keys[pygame.K_LEFT]:
        mario.que_hace = "Izquierda"
    elif(keys[pygame.K_SPACE]):
        mario.que_hace = "Salta"

    else:
        que_hace = "Quieto"

    PANTALLA.blit(fondo, (0,0))
    

    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])
    mario.actualizar(PANTALLA, plataformas)

    if obtener_modo():
        #pygame.draw.rect(pantalla, "red", piso, 3)
        pygame.draw.rect(pantalla, "blue", mario.rectangulo_principal, 3)


    pygame.display.update()


pygame.quit()


