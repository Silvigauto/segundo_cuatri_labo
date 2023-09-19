import pygame,sys
from pygame.locals import *

pygame.init()

BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)
AZUL_CLARO = (0,150,255)

PANTALLA = pygame.display.set_mode((500,500))
pygame.display.set_caption('mi primer juego')

PANTALLA.fill(BLANCO)
'''
#LINEAS
#donde dibujo, el color, coordenadas x1y1 x2y2, grosor, si no defino, el pixel es 1 --> y1 e y2 tienen que ser iguales para que sea una linea recta
pygame.draw.line(PANTALLA, VERDE, (100,100), (200,100), 2 )
#linea decreciente 
pygame.draw.line(PANTALLA, AZUL, (100,100), (350,250), 2 )
#linea creciente y1 > y2 / x1 < x2
pygame.draw.line(PANTALLA, AZUL, (100,100), (350,10), 2 )
#linea vertical
pygame.draw.line(PANTALLA, NEGRO, (100,100), (100,10), 2 )
'''

'''
#RECTANGULOS
#recibe --> la superficie donde se va a dibujar, el valor x,y (coordendada inicial) y width y height, parametro opcional, el ancho del borde (rellenado)
pygame.draw.rect(PANTALLA, VERDE, (50,50,100,100), 2) #cuadrado
pygame.draw.rect(PANTALLA, VERDE, (100,75,100,300), 2) #rectangulo
'''

'''
#CIRCULOS
#recibe--> en que superficie se dibuja,color, el valor de x,y (punto centro del circulo) y el radio, parametro opcional relleno 
pygame.draw.circle(PANTALLA, ROJO, (60,60), 50, 2)

pygame.draw.circle(PANTALLA, NEGRO, (250,250), 50, 2)
'''

'''
#OVALOS
#recibe -->en que superficie se dibuja, color, xy donde empieza largo y alto, parametro opcional relleno
pygame.draw.ellipse(PANTALLA, AZUL, (50,50,150,200))
'''


'''
#TRIANGULOS --> necesito 3 puntos
#           vertice izq  inf /vertice superior/ vertice der inf
#puntos = [(100,300), (100,100), (150,300)] --> tringualo rectangulo
puntos = [(50,300), (100,100), (150,300)] #--> triangulo comun
pygame.draw.polygon(PANTALLA, AZUL, puntos, 2)
'''







while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
