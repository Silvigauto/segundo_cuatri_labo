from modulos.characters.Falling_object import FallingObject
from modulos.config import Config
from modulos.values.colores import * 
from modulos.characters.heroe import Heroe

import pygame as py

class Game(Config):
    def __init__(self, size, FPS, caption='Title', icon="") -> None:
        super().__init__(size, FPS, caption, icon)
        self.set_heroe()
        self.set_falling_objects(28)
        falling = FallingObject((50,50), (0,0), self.size)

        self.pressed_keys = []

    def set_heroe(self):
        x = self.size[0] //2
        y = self.size[1] - 160
        self.heroe = Heroe((50,75), (x,y), 10) #hacer el constructor

    def set_falling_objects(self, size):
        self.falling_objects = FallingObject.create_list(size)

    def move_heroe(self):
        if self.pressed_keys[py.K_RIGHT]:
            self.heroe.move_right(self.size[0])
        elif self.pressed_keys[py.K_LEFT]:
            self.heroe.move_left(0)
        elif self.pressed_keys[py.K_UP]:
            self.heroe.move_up()
        elif self.pressed_keys[py.K_DOWN]:
            self.heroe.move_down()
        else:
            self.heroe.stop()

    def blit_heroe(self):
        #self.heroe.move_right()
        self.screen.blit(self.heroe.image, self.heroe.rect)

    def blit_falling_objects(self):
        for fo in self.falling_objects:
            self.screen.blit(fo.image, fo.rect)


    def init(self):
        py.init()

        while self.running:
            self.fill_screen(PURPURA)
            self.clock.tick(self.FPS)


            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running  = False
            
            self.get_pressed()

            self.move_heroe()

            self.blit_heroe()

            self.blit_falling_objects()

            py.display.flip()

        py.quit()

    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()