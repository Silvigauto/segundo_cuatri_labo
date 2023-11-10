import pygame



def rotar_imagenes(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = pygame.transform.flip(imagenes[i], True, False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes


def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho,alto))


personaje_quieto = [pygame.image.load("18_clase_03_11_presencial\\corre\\0.png")]

personaje_derecha = [pygame.image.load("18_clase_03_11_presencial\\corre\\1.png"), 
                            pygame.image.load("18_clase_03_11_presencial\\corre\\2.png")]

personaje_izquierda = rotar_imagenes(personaje_derecha)

personaje_salta = [pygame.image.load("18_clase_03_11_presencial\\corre\\3.png")]

super_mario_derecha = [pygame.image.load(r"19_clase_09_11\corre\sm1.png"), 
            pygame.image.load(r"19_clase_09_11\corre\sm2.png"),
            pygame.image.load(r"19_clase_09_11\corre\sm3.png"),
            pygame.image.load(r"19_clase_09_11\corre\sm4.png")]

super_mario_izquierda = rotar_imagenes(super_mario_derecha) 

super_mario_quieto = [pygame.image.load(r"19_clase_09_11\corre\sm6.png")]

super_mario_salta = [pygame.image.load(r"19_clase_09_11\corre\sm5.png")]

enemigo_camina = [pygame.image.load("18_clase_03_11_presencial\corre\ene1.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene2.png")]

enemigo_aplasta = [pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png"),
                pygame.image.load("18_clase_03_11_presencial\corre\ene3.png")]

flor_fuego = [pygame.image.load("19_clase_09_11\corre\\flor.png")]