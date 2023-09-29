import pygame
import sys
import random

def definir_color()->tuple:
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    background = (red,green,blue)

    return background


pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')

BLANCO = (255,255,255)
bandera = True

player_color = (0,0,255)

#genera un temporizador, recibe el evento personalizado y cada cuantos milisegundos se dispara

font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

CAMBIO_COLOR = pygame.USEREVENT + 1 
pygame.time.set_timer(CAMBIO_COLOR, 2000)
background = (0,0,0)

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == CAMBIO_COLOR:
            background = definir_color()

            

    screen.fill(background)


    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()