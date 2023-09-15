from os import system
system('cls')

from data import lista_bzrp
from funcionesbiza import *


while True:
    respuesta = int(input("1.Temas mas vistos\n2.Duracion Promedio\n3.Cantidad de temas sobre el promedio\n4.temas mas largos\n5.Salir\nElija una opcion:"))
    match respuesta:
        case 1:
            buscar_temas_maximos_key(lista_bzrp, 'views', 'El temas mas visto es')
        case 2:
            #tiempo promedio 
            promedio = calcular_promedio(lista_bzrp)
            print(promedio)
        case 3:
            #temas que superan el promedio
            promedio = calcular_promedio(lista_bzrp)
            for video in lista_bzrp:
                duracion = video['length']
                nombre = video['title']

                if duracion > promedio:
                    print(nombre)
        case 4:
            buscar_temas_maximos_key(lista_bzrp, 'length', 'Duracion mas larga')
        case 5:
            break
