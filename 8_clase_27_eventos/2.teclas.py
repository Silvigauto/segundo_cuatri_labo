import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')
bandera = True

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            nombre = pygame.key.name(event.key) #convierto el valor ascii a su equivalente
            print(f'tecla presionada: {nombre} ') #.key devuelve el valor ascii de cada tecla
        

pygame.quit()
sys.exit()