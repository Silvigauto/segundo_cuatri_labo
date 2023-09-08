import pygame

BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)



pygame.init()
#recibe una tupla --> LARGO, ALTO
VENTANA = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mi primer ventana en pygame")

#primero cargar la imagen en pygame
icono = pygame.image.load("2clase\icono.png")
pygame.display.set_icon(icono)
#llenar con color la ventana
VENTANA.fill(AZUL)

flag = True

while flag == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    pygame.display.update()

pygame.quit()