import pygame as py

from modulos.values.eorientation import EOrientation

class Object:

    def __init__(self, size_surface, position) -> None:
        # self.speed = 0

        self.image = py.Surface(size_surface)#creamos la img del tamaño del parametro

        self.rect = self.image.get_rect()#sacamos el rectangulo
        
        self.rect.x = position[0] #donde seran las posiciones iniciales
        self.rect.y = position[1]

        self.direction = EOrientation.IDLE #direccion donde se dirige(inicia quieto)
        
        self.set_speed(0) 
    
    def set_speed(self, speed):#metodo para que nos puedan cambiar la velocidad
        self.speed = speed

    def move_right(self, speed=None):
        if speed:
            self.set_speed(speed=None)
        self.direction = EOrientation.RIGHT
        self.move()

    def move_left(self, speed=None):
        if speed:
            self.set_speed(speed=None)
        self.direction = EOrientation.LEFT
        self.move()

    def move_up(self, speed=None):
        if speed:
            self.set_speed(speed=None)
        self.direction = EOrientation.UP
        self.move()
    
    def move_down(self, speed=None):
        if speed:
            self.set_speed(speed)
        self.direction = EOrientation.DOWN
        self.move()
    
    def stop(self):
        self.direction = EOrientation.IDLE
        self.move()

    def move(self): #metodo general de movimiento (en este metodo no restringimos los limites de la pantalla, eso se cambia en cada objeto creado que herede)
        if self.direction == EOrientation.LEFT:
            self.rect.x -= self.speed
        elif self.direction == EOrientation.RIGHT:
            self.rect.x += self.speed
        elif self.direction == EOrientation.UP:
            self.rect.y -= self.speed
        elif self.direction == EOrientation.DOWN:
            self.rect.y += self.speed
        elif self.direction == EOrientation.IDLE:
            pass
        else:
            raise ValueError('Invalid direction')
        

    def blit(self, screen):
        screen.blit(self.image, self.rect)
            