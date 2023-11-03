import pygame as py


#lo que pongo en el constructor no cambia
#si lo pongo en el metodo lo pedo modificar dsp

class Config:
    def __init__(self, size,FPS, caption = 'Title',icon = "") -> None:
        py.mixer.init()
        self.size = size
        self.FPS = FPS
        self.clock = py.time.Clock() #guardar el reloj en la instancia
        self.set_caption(caption)
        self.running = True
        self.screen = py.display.set_mode(self.size)


    def set_caption(self, caption): #esta es del constructor (metodo wrapper)
        py.display.set_caption(caption) #esta es de pygame

    def set_icon(self,icon):
        pass

    def set_fps(self,FPS):
        self.FPS = FPS

    def set_music(self, music):
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.2)
        self.play_music()
    
    def set_volume(self,volume):
        self.music.set_volume(volume)
    
    def play_music(self):
        self.music.play()
    
    def stop_music(self):
        self.music.stop()

    def set_background_image(self):
        pass

    def set_fuente(self):
        pass

    def fill_screen(self, color=None):
        if color != None:
            self.screen.fill(color)
