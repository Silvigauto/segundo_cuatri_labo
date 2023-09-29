import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')

BLANCO = (255,255,255)
bandera = True
clock = pygame.time.Clock()

player_color = (0,0,255)

#genera un temporizador, recibe el evento personalizado y cada cuantos milisegundos se dispara
mensaje = 'hola 1bd'
x,y = 100,100
font = pygame.font.SysFont("Arial", 30)

pygame.time.set_timer(pygame.USEREVENT, 1000)

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.USEREVENT:
            x += 10

    screen.fill((0,0,0))

    texto = font.render(mensaje, True,BLANCO)
    screen.blit(texto, (x,y))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()