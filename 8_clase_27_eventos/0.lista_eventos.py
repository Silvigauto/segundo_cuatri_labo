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
        print(event)

pygame.quit()
sys.exit()