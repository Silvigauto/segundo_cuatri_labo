from data_stark import *
from os import system
system('cls')


diccionario = {"nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""}

print('DICCIONARIO ENTERO')
print(diccionario)

print(diccionario['nombre'])

print('CLAVES')
for clave in diccionario:
    print(clave)

print('VALORES')
for clave in diccionario:
    print(diccionario[clave]) #imprime todos los valores --> prueba:diccionario/ dic

diccionario['nombre'] = 'rocio'
diccionario['peso'] = 'silvina'
diccionario['hola'] = 'probando'

'''
match opcion:
            case 1:
                datos_normalizados = stark_normalizar_datos(lista)
                if datos_normalizados == False:
                    print('ya se ha normalizado la lista anteriormente')
            case 2:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                for heroe in lista_no_binarios:
                        print(obtener_nombre_y_dato(heroe, 'genero'))
            case 3:
                lista_femeninos = obtener_superheroes_por_genero(lista, 'F')
                maximo = obtener_maximo(lista_femeninos, 'altura')
                lista_coincidencias = obtener_dato_cantidad(lista_femeninos, maximo, 'altura')
                if lista_coincidencias == False:
                    print('hubo un error en la lista')
                elif len(lista_coincidencias) > 0:
                    for heroe in lista_coincidencias:
                        print(obtener_nombre_y_dato(heroe, 'altura'))

                
            case 4:
                lista_masculinos = obtener_superheroes_por_genero(lista, 'M')
                maximo = obtener_maximo(lista_masculinos, 'altura')
                lista_coincidencias = obtener_dato_cantidad(lista_masculinos, maximo, 'altura')
                if lista_coincidencias == False:
                    print('hubo un error en la lista')
                elif len(lista_coincidencias) > 0:
                    for heroe in lista_coincidencias:
                        print(obtener_nombre_y_dato(heroe, 'altura'))

            case 5:
                lista_masculinos = obtener_superheroes_por_genero(lista, 'M')
                minimo = obtener_minimo(lista_masculinos, 'fuerza')
                lista_coincidencias = obtener_dato_cantidad(lista_masculinos, minimo, 'fuerza')
                if lista_coincidencias == False:
                    print('hubo un error en la lista')
                elif len(lista_coincidencias) > 0:
                    for heroe in lista_coincidencias:
                        print(obtener_nombre_y_dato(heroe, 'fuerza'))
            case 6:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                minimo = obtener_minimo(lista_no_binarios, 'fuerza')
                lista_coincidencias = obtener_dato_cantidad(lista_no_binarios, minimo, 'fuerza')
                if lista_coincidencias == False:
                    print('hubo un error en la lista')
                elif len(lista_coincidencias) > 0:
                    for heroe in lista_coincidencias:
                        print(obtener_nombre_y_dato(heroe, 'fuerza'))


'''