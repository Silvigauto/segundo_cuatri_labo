from configuraciones import * 

class Personaje:
    def __init__(self, animaciones:dict,velocidad:int, tamaño, pos_x, pos_y) -> None:
        self.animaciones = animaciones
        #el asterico desempaqueta la tupla(posicionalmente)
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectamgulo_principal.x = pos_x
        self.rectamgulo_principal.y = pos_y

        self.velocidad = velocidad
        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Quieto"]

        self.desplazamiento_y = 0
        self.potencia_salto = -15 #sube
        self.limite_velocidad_salto = 15 #baja 
        self.gravedad = 1
        self.esta_saltando = False
    
    def actualizar(self, pantalla,plataformas):
        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Derecha"]
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Izquierda"]
                    self.animar(pantalla)
                self.caminar(pantalla)

            case "Quieto":
                if not self.esta_saltando:

                    self.animacion_actual = self.animaciones["Quieto"]
                    self.animar(pantalla)
            
            case "Salta":
                if not self.esta_saltando:

                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["Salta"]
        
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
            self.rectangulo_principal.x += self.velocidad_actual

    def aplicar_gravedad(self, pantalla,piso,plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y 
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.rectangulo_principal.bottom = piso["rectangulo"].top
                break
            
            else:
                self.esta_saltando = True