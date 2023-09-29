import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')

BLANCO = (255,255,255)

player_color = (0,0,255)

clock = pygame.time.Clock()

width_recatangle = 50
height_rectangle = 50

BLANCO = (255,255,255)
x,y = 100,100
velocidad = 5
direccion = 1 #-1-> izquierda
pygame.time.set_timer(pygame.USEREVENT, 100)

bandera = True
while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.USEREVENT:
            x += velocidad * direccion
            if x <= 0 or x >= screen_width-width_recatangle:
                direccion *= -1
    
    screen.fill((0,0,0))

    pygame.draw.rect(screen, BLANCO, (x,y,width_recatangle,height_rectangle))

    pygame.display.update()

    clock.tick(15)

pygame.quit()
sys.exit()