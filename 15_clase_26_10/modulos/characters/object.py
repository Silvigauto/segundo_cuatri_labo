import pygame as py
from modulos.values.eorientation import EOrientation


class Object:
    def __init__(self, size_surface, position) -> None:
        #self.speed = 0
        self.set_speed(0) #si utlizo el metodo no hace falta q cambie en todos lados

        self.image = py.Surface(size_surface)

        self.rect = self.image.get_rect()

        self.rect.x = position[0]
        self.rect.y = position[1]

        self.direction = EOrientation.IDLE

    def set_speed(self,speed):
        self.speed = speed

    
    
    def move_right(self):
        self.direction = EOrientation.RIGHT
        self.move()

    def move_left(self):
        self.direction = EOrientation.LEFT
        self.move()
    
    def move_up(self):
        self.direction = EOrientation.UP
        self.move()
    
    def move_down(self):
        self.direction = EOrientation.DOWN
        self.move()
    
    def stop(self):
        self.direction = EOrientation.IDLE
        self.move()

    def move(self):
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

    
