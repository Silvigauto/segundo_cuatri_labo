import pygame
import sys

pygame.init()

BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('mi ventana')

PANTALLA.fill(BLANCO)

#pygame.draw.line(PANTALLA, AZUL, (100,100), (350,100), 5)

#x,y,largo,alto
#pygame.draw.rect(PANTALLA, VERDE, (50,50,100,100), 2)

#circulo --> x,y (epicentro),radio/ si no especifico la linea, se rellena todo el circulo
#pygame.draw.circle(PANTALLA,VERDE, (150,75), 50, 1)

puntos = [(100,300), (100,100), (150,100)]
#triangulo
pygame.draw.polygon(PANTALLA, AZUL, puntos, 2)

while True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
