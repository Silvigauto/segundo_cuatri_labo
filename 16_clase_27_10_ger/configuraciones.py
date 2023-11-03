import pygame

def reescalar_imagenes(lista_animaciones, ancho, alto):
    for clave in lista_animaciones:
        lista = lista_animaciones[clave]
        for i in range(len(lista)):
            img = lista[i]
            lista[i] = pygame.transform.scale(img, (ancho,alto))


personaje_quieto = [pygame.image.load("corre\\0.png")]

personaje_camina_derecha = [pygame.image.load("corre\\1.png"),
                            pygame.image.load("corre\\2.png")]

personaje_salta = [pygame.image.load("corre\\3.png")]