import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('eventos de teclado')
x,y = 100,300

bandera = True
clock = pygame.time.Clock()

player_color = (0,0,255)


MOVE_UP_EVENT = pygame.USEREVENT + 0 #este evento es un valor entero
MOVE_DOWN_EVENT = pygame.USEREVENT + 1


while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.event.post(pygame.event.Event(MOVE_UP_EVENT))
            elif event.key == pygame.K_s:
                pygame.event.post(pygame.event.Event(MOVE_DOWN_EVENT))
        elif event.type == MOVE_UP_EVENT:
            y -= 10
        elif event.type == MOVE_DOWN_EVENT:
            y += 10

    screen.fill((0,0,0))
    pygame.draw.rect(screen, player_color,(x, y,50,50) )
    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()