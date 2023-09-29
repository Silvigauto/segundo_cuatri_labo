import pygame
import sys


screen_width = 400
screen_height = 400
width_recatangle = 50
height_rectangle = 50


x,y = 100,100
velocidad = 5
direccion = 1 #-1-> izquierda


BLANCO = (255,255,255)
ROJO = (255,0,0)
color_rectanuglo = BLANCO

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100)

bandera = True

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= velocidad
            elif event.key == pygame.K_RIGHT:
                x += velocidad
            elif event.key == pygame.K_UP:
                y -= velocidad
            elif event.key == pygame.K_DOWN:
                y += velocidad
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_x = event.pos[0]
            pos_y = event.pos[1]

            if pos_x >= x and pos_x <= (x+width_recatangle) and pos_y >= y and pos_y <= (y+height_rectangle):
                color_rectanuglo = ROJO
            else:
                color_rectanuglo = BLANCO

    screen.fill((0,0,0))

    pygame.draw.rect(screen, color_rectanuglo, (x,y,width_recatangle,height_rectangle))

    pygame.display.update()

    clock.tick(15)

pygame.quit()
sys.exit()