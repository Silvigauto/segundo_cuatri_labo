import pygame,sys
from pygame.locals import *

from funciones import *

#pygame.init() --> en configuraciones

#-------------------------BUCLE------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    PANTALLA.blit(fondo, (0, 0))

    dibujar_y_mostrar_resultado_figura(figura_rectangulo)
    
    pygame.display.update()
