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
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            print(f'({x}, {y})')
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                print('ruedita para arriba')
            else:
                print('ruedita para abajo')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("izquierdo")
            elif event.button == 3:
                print('derecho')
            elif event.button == 2:
                print('ruedita')

pygame.quit()
sys.exit()