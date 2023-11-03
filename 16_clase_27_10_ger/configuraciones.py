import pygame

def reescalar_imagenes(lista_animaciones, ancho, alto):
    for clave in lista_animaciones:
        lista = lista_animaciones[clave]
        for i in range(len(lista)):
            img = lista[i]
            lista[i] = pygame.transform.scale(img, (ancho,alto))


personaje_quieto = [pygame.image.load("16_clase_27_10_ger\corre\\0.png")]

personaje_camina_derecha = [pygame.image.load("16_clase_27_10_ger\corre\\1.png"),
                            pygame.image.load("16_clase_27_10_ger\corre\\2.png")]

personaje_salta = [pygame.image.load("16_clase_27_10_ger\corre\\3.png")]