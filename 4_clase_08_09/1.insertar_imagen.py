import pygame

pygame.init()
#recibe una tupla --> LARGO, ALTO
ventana = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Mi primer ventana ")

imagen = pygame.image.load("4_clase_08_09\gatito.png")
imagen = pygame.transform.scale(imagen, (200,200))
#otra_imagen = pygame.image.load("4_clase_08_09\perro.jpg")

flag_run = True

while flag_run == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    #recibe la imagen a blitear y las coordenadas
    ventana.blit(imagen, (50,50))
    #ventana.blit(otra_imagen, (200,200))
    pygame.display.update()
pygame.quit()