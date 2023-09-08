from os import system
system('cls')

'''
Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
'''


'''
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''

##github

from data_stark import *

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
for heroe in lista_personajes:
    nombre = heroe['nombre']
    identidad = heroe['identidad']
    empresa = heroe['empresa']
    altura = float(heroe['altura'])
    peso = float(heroe['peso'])
    genero = heroe['genero']
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']
    fuerza = int(heroe['fuerza'])
    inteligencia = heroe['inteligencia']

    #print(f'{nombre:20}{identidad:30}{empresa:15}{altura}/{peso}/{genero}/{color_ojos}/{color_pelo}/{fuerza}/{inteligencia}')

#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
bandera_primero = True
for heroe in lista_personajes:
    fuerza = int(heroe['fuerza'])
    if bandera_primero == True or fuerza > maxima_fuerza:
        maxima_fuerza = fuerza
        bandera_primero == False

print(f'Maxima fuerza: {maxima_fuerza}')
for heroe in lista_personajes:
    pass