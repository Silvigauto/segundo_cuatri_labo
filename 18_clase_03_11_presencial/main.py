import pygame
from pygame.locals import *
from configuraciones import *
from Modo import *
from ClassPersonaje import * 
from ClassEnemigo import * 

pygame.init()

def crear_plataforma(visible,tamaño, x,y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma




W, H = 1200,680
FPS = 18

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# Fondo
fondo = pygame.image.load("18_clase_03_11_presencial\corre\\fondo.jpg")
fondo = pygame.transform.scale(fondo, (W, H))


# x_inicial = H/2 - 400
# y_inicial = 760



contador_pasos = 0

#personaje_izquierda = rotar_imagenes(personaje_derecha)

diccionario = {}
diccionario["Quieto"] = personaje_quieto
diccionario["Derecha"] = personaje_derecha
diccionario["Izquierda"] = personaje_izquierda
diccionario["Salta"] = personaje_salta


mario = Personaje(diccionario, (70,60), 100, 555,5 ) #POSICIONES DE MARIO
reescalar_imagenes(diccionario, 80,70)


#PISO

#piso = pygame.Rect(0,550,W,20)
piso = crear_plataforma(False, (W,20), 0,H-60) #POSICION DEL PISO

plataforma_caño = crear_plataforma(True, (100,100), 850, 525, "18_clase_03_11_presencial\corre\Caño (2).png")

plataforma_invisible = crear_plataforma(False, (220,20),893,459, "")
plataformas = [piso, plataforma_caño, plataforma_invisible]


#ENEMIGOS
diccionario_animaciones = {"izquierda": enemigo_camina, "aplasta":enemigo_aplasta}
un_enemigo = Enemigo(diccionario_animaciones)

#OTRO ENEMIGO
otro = Enemigo(diccionario_animaciones)
otro.rectangulo_principal.x = 500

#CONFIGURACION ENEMIGO APLASTADO
d = {"aplasta": diccionario_animaciones["aplasta"]}
reescalar_imagenes(d,50,20)
lista_enemigos = [un_enemigo, otro]

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == MOUSEBUTTONDOWN:
            print(evento.pos) 
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
        mario.que_hace = "Quieto"

    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])

    mario.verificar_colision_enemigo(lista_enemigos, PANTALLA)
    mario.actualizar(PANTALLA,plataformas)
    un_enemigo.actualizar(PANTALLA)

    for i in range(len(lista_enemigos)):
        if lista_enemigos[i].esta_muerto:
            
            del lista_enemigos[i]
            break

    
    if obtener_modo():
        #pygame.draw.rect(pantalla, "red", piso, 3)
        pygame.draw.rect(PANTALLA, "blue", mario.rectangulo_principal, 3)

        for plataforma in plataformas:
            pygame.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)



    pygame.display.update()


pygame.quit()


