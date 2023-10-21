class Personaje:
    #primero defino el constructor de la clase, no tienen retorno
    def __init__(self, id_personaje, nombre_personaje, puede_volar, poder:int,  usa_nano = False) -> None:  #metodo constructor
        self.__id = id_personaje #PUBLICO
        self.__nombre = nombre_personaje #PRIVADO
        self.__puede_volar = puede_volar
        self.__usa_nano = usa_nano
        self.__poder = poder

        #self.id --> atributo del personaje 

    def mostrar(self):
        print(f'{self.id} - {self.__nombre} - {self.__puede_volar} - {self.__usa_nano}')

    def retornar_descripcion(self) -> str:
        descripcion = f'{self.__id} - {self.__nombre} - {self.__puede_volar} - {self.__usa_nano}'
        return descripcion
    
    def luchar(self, otro_personaje):
        print(f"{self.__nombre} VS. {otro_personaje.__nombre}")
        if(self.__poder > otro_personaje.poder):
            print(f"Gano {self.__nombre}")
        elif self.__poder < otro_personaje.poder:
            print(f"Gano {otro_personaje.__nombre}")
        else:
            print("Hubo empate")

    #GETTERS Y SETTERS  --> ACCEDER Y MODIFICAR

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre.strip().title()
    
    def set_id(self, id):
        retorno = False
        if id > 0:
            self.__id = id
            retorno = True
        return retorno

'''
abstraccion
herencia

'''