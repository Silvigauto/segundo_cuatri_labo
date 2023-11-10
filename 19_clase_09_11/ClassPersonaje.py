from configuraciones import * 
from ClassEnemigo import Enemigo 
import pygame

class Personaje:
    def __init__(self, animaciones:dict, tamaño, pos_x, pos_y, velocidad) -> None:
        self.animaciones = animaciones
        #el asterico desempaqueta la tupla(posicionalmente)
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y

        self.velocidad = velocidad

        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto"]

        self.desplazamiento_y = 0
        self.potencia_salto = -25 #sube
        self.limite_velocidad_salto = 15 #baja 
        self.gravedad = 1
        self.esta_saltando = False

        self.habilidad_especial = False
        self.tiempo = 10000 #en milisegundos 10 seg
        self.tiempo_anterior = 0
    
    def actualizar(self, pantalla,piso):

        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual > self.tiempo_anterior + self.tiempo:
            self.habilidad_especial = False

        accion = ""
        
        if self.habilidad_especial:
            match self.que_hace:
                case "Derecha":
                    accion = "Super_Derecha"
                case "Izquierda":
                    accion = "Super_Izquierda"
                case "Quieto":
                    accion = "Super_Quieto"
                case "Salta":
                    accion = "Super_Salta"
            
            self.animacion_actual = self.animaciones[accion]
        else:
            self.animacion_actual = self.animaciones[self.que_hace]


        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.caminar(pantalla)

            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla)
        
            case "Salta":
                if not self.esta_saltando: #para que no se superpongan las imagenes
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animar(pantalla)
        
        self.aplicar_gravedad(pantalla,piso) #siempre se aplica gravedad

    def animar(self, pantalla): 
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        self.contador_pasos += 1

    def caminar(self, pantalla):
        velocidad_actual = self.velocidad #me guardo una copia de la velocidad original
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1

        nueva_x = self.rectangulo_principal.x + velocidad_actual
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            self.rectangulo_principal.x += velocidad_actual
    
    def verificar_colision_enemigo(self,lista_enemigos:list["Enemigo"], pantalla):
        for enemigo in lista_enemigos:
            if self.rectangulo_principal.colliderect(enemigo.rectangulo_principal):
                enemigo.muriendo = True
                enemigo.rectangulo_principal.y  += 20
                enemigo.animacion_actual = enemigo.animaciones["aplasta"]
                enemigo.animar(pantalla)
                # enemigo.esta_muerto = True
                # pygame.time.delay(500)
                # lista_enemigos.remove(enemigo)
    
                


    def aplicar_gravedad(self, pantalla,plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y 
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for piso in plataformas:
            if not piso["premio"]:
                if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                    self.desplazamiento_y = 0 #reinicio el y (y todos los atributos que tenia que ver con el salto)
                    self.esta_saltando = False #cuando colisiona con el piso, deja de saltar
                    self.rectangulo_principal.bottom = piso["rectangulo"].top #hago que coincida asi no se entierran los pies
                    break
            
                else:
                    self.esta_saltando = True
    
    def romper_bloque(self, lista_plataformas, flor):
        for plataforma in lista_plataformas:
            if plataforma["premio"]:
                if self.rectangulo_principal.colliderect(plataforma["rectangulo"]):
                    flor["descubierta"] = True
                    plataforma["premio"] = False

    def verificar_colision_flor(self, flor):
        if flor["descubierta"] and self.rectangulo_principal.colliderect(flor["rectangulo"]):
            #cambio ambos estados de la flor asi no se blitea
            flor["tocada"] = True
            flor["descubierta"] = False
            self.tiempo_anterior = pygame.time.get_ticks()
            self.habilidad_especial = True