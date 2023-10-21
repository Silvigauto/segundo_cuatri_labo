from Class_Personaje import Personaje

personaje = Personaje(1, "IronMan", True,150, True)
# personaje.mostrar()

otro_personaje = Personaje(6, "Thor", True, 190)

# otro_personaje.mostrar()

# personaje.luchar(otro_personaje)

tercer_personaje = Personaje(7, "capitan america", False, 200)

# otro_personaje.luchar(tercer_personaje)#relacion de colaboracion (entre los objetos)

if personaje.set_id(10):
    print("esta todo ok")
    print(personaje.get_nombre())

    personaje.set_nombre("       superior ironman     ") 
    print(personaje.get_nombre())
else:
    print('el id no es valido')
