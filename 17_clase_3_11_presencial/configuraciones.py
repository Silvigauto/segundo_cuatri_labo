import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    pass

def reescalalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho,alto))


# personaje_quieto = [pygame.image.load("clase15(desarrollo)\\assets\\0.png")]
# personaje_camina_derecha = [pygame.image.load(
#     "clase15(desarrollo)\\assets\\1.png"), pygame.image.load(
#     "clase15(desarrollo)\\assets\\2.png")]
# personaje_salta = [pygame.image.load("clase15(desarrollo)\\assets\\3.png")]
