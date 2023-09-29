import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')

bandera = True
clock = pygame.time.Clock()

tiempo_inicial = pygame.time.get_ticks()

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
    
    tiempo_actual = pygame.time.get_ticks() #milisegundos
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    print(f'{(tiempo_transcurrido*0.001):.02f}')

    clock.tick(60)

pygame.quit()
sys.exit()