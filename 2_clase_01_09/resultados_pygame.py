import pygame

from ejercicio_01 import *

lista_resultados = [f'Contador masculino: {contador}', f'Porcentaje: {porcentaje}', f'Maxima Edad: {maxima_edad}']
lista_resultados_str = []

for resultado in lista_resultados:
    resultado_string = str(resultado)
    lista_resultados_str.append(resultado_string)

CELESTE = (73,160,174)
ROJO = (255,0,0)
VERDE = (208,222,86)
GRIS = (96,96,96)

pygame.init()
VENTANA = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Mi primer ventana en pygame")

icono = pygame.image.load("2_clase_01_09\icono.png")
pygame.display.set_icon(icono)
VENTANA.fill(CELESTE)

fuente = pygame.font.SysFont("Arial", 30)#--> esto devuelve una superficie

flag = True
while flag == True:
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    for resultado in lista_resultados_str:
        texto = fuente.render(resultado, False, GRIS, VERDE )
        #antes de hacer el update, recibe una surface y las coordenadas donde se van a mostrar
        VENTANA.blit(texto, (50,y) )
        y += 40
    
    y = 170
    for coincidencia in lista_maxima_edad:
        texto = fuente.render(coincidencia, False, GRIS, VERDE )
        #antes de hacer el update, recibe una surface y las coordenadas donde se van a mostrar
        VENTANA.blit(texto, (50,y) )
        y += 40

    pygame.display.update()

pygame.quit()