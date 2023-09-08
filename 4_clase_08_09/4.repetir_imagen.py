import pygame

pygame.init()
#recibe una tupla --> LARGO, ALTO
ventana = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Mi primer ventana ")
OLIVA = (128, 128, 0)
a1 = {'nombre': 'michi', 'edad':2, 'imagen': 'gatito.jpg'}

imagen = pygame.image.load("4_clase_08_09\gatito.png")
imagen = pygame.transform.scale(imagen, (100,100))
imagen = pygame.transform.rotate(imagen,90)
#otra_imagen = pygame.image.load("4_clase_08_09\perro.jpg")

flag_run = True
x = 50
ventana.fill(OLIVA)
while flag_run == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    ventana.blit(imagen, (x,50))
    #ventana.blit(otra_imagen, (200,200))
    x+=110 #en base al tamaño de la iamgen

    if x >= 1400:
        x = 50
        
    pygame.display.update()
pygame.quit()