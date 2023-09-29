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

custom_event = pygame.USEREVENT



while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.event.post(pygame.event.Event(custom_event)) #se agrega el evento a la lista de eventos
        elif event.type == custom_event:
            print('presiona la tecla derecha mediando un evento personalizado')

    

    clock.tick(60)

pygame.quit()
sys.exit()