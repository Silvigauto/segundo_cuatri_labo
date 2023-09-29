
from os import system
system('cls')
import re
from data_stark import *

'''
Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
En el caso que el nombre del personaje contenga el artículo ‘the’ se deberá omitir de las iniciales
Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.
ATENCIÓN: Usar regex

'''
#1.1
def extraer_iniciales(nombre_heroe:str):
    if len(nombre_heroe) != 0:
        nombre_heroe = re.sub(' the', '', nombre_heroe)
        nombre_heroe = re.sub('-', ' ', nombre_heroe)
        nombre_heroe = re.split(' ',nombre_heroe)

        lista_iniciales = []
        for palabra in nombre_heroe:
            lista_iniciales.append(palabra[0])
        
        separador = '.'
        iniciales_heroe = separador.join(lista_iniciales)
        return iniciales_heroe
    else:
        return 'N/A'

'''
Crear la función obtener_dato_formato’ la cual recibirá como parámetro:
dato: un string con un dato especifico
La función deberá convertir el dato pasado a minúsculas y con formato snake_case 
por ejemplo: Howard the Duck -> howard_the_duck
La función deberá validar:
Que el dato recibido sea del tipo str
En caso de encontrar algún error retornar False, caso contrario el nombre con el formato especificado
ATENCIÓN: Usar regex

'''

#1.2
def obtener_dato_formato(dato:str):
    dato_formato = False
    if type(dato) == str:
        dato = dato.lower()
        dato = re.split(' ',dato)
        separador = '_'
        dato_formato = separador.join(dato)

    return dato_formato

'''
Crear la función ‘stark_imprimir_nombre_con_iniciales’ la cual recibirá como parámetro:
nombre_heroe: un string con el nombre del personaje
Se deberá validar:
Que el dato recibido sea del tipo diccionario
Que el  diccionario contengan la clave ‘nombre’  
La función deberá imprimir el dato en cuestión con el siguiente formato
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
Si el superhéroe es Howard the Duck se deberá mostrar 
* howard_the_duck (H.W.)
La función deberá devolver True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error

'''

#1.3
#??validar que sea diccionario
def stark_imprimir_nombre_con_iniciales(nombre_heroe:dict):
    finalizacion =False
    if type(nombre_heroe) == dict:
        for clave in nombre_heroe:
            if clave == 'nombre':
                iniciales = extraer_iniciales(nombre_heroe['nombre'])
                nombre_formato = obtener_dato_formato(nombre_heroe['nombre'])
                print(f'* {nombre_formato} ({iniciales}) ')
                finalizacion = True
    return finalizacion

'''
1.4 Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
lista_heroes: la lista de personajes
La función deberá utilizar la función anterior 
Luego deberá imprimir la lista completa de los nombres de los personajes con el mismo formato de la anterior
	Se deberá validar:
Que lista_heroes sea del tipo lista
Que la lista contenga al menos un elemento
La función retornara True si salió todo bien y False si ocurrió algún error

'''
#1.4
def stark_imprimir_nombres_con_iniciales1(lista:list):
    if type(lista) == list and len(lista) != 0:
        for heroe in lista:
            stark_imprimir_nombre_con_iniciales(heroe)

'''
Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetro:
diccionario de un héroe
id_heroe (int)
La función deberá generar un string con el siguiente formato:
GENERO-X00…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por último el identificador recibido.  Todos los códigos generados 
deben tener como máximo 10 caracteres (contando todos los caracteres, inclusive el guión). Se deberá completar con ceros para 
que todos queden del mismo largo.
Dependiendo del género el primer número del código variará
En caso de que sea un superhéroe de género M -> el código comenzará en 1
En caso de que sea un superhéroe de género F-> el código comenzará en 2
En caso de que sea un superhéroe de género NB-> el código comenzará en 0
Algunos ejemplos:
F-20000001 (10 caracteres)
M-10000002 (10 caracteres)
NB-0000010 (10 caracteres)
La función deberá validar:
El género no se encuentre vacío y este dentro de los valores esperados (‘M’,  ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse correctamente retornar el código generado.
'''
#2.1
def generar_codigo_heroe(heroe:dict, id_heroe:int):
    codigo_heroe = 'N/A'
    if len(heroe['genero']) > 0:
        genero_heroe = heroe['genero']
        if genero_heroe == 'F' or genero_heroe == 'M' or genero_heroe == 'NB':
            match genero_heroe:
                case 'M':
                    id = '1'
                case 'F':
                    id = '2'
                case 'NB':
                    id = '0'
            if len(genero_heroe) == 1:
                id_heroe = str(id_heroe).zfill(7)
            else:
                id_heroe = str(id_heroe).zfill(6)
            codigo_heroe = f'{genero_heroe}-{id}{id_heroe}'
    return codigo_heroe


'''
Crear la función ‘stark_generar_codigos_heroes’  la cual recibirá como parametro:
lista_heroes: la lista de personajes:
La función deberá iterar la lista de personajes y generar cada uno de los códigos
El código del héroe (id_heroe) surge de la posición del mismo dentro de la lista_heroes (comenzando por el 1).
Reutilizar la función anterior pasándole como argumentos el id_heroe correspondiente
Guardar en un string cada uno de los heroes con el siguiente formato y al final de toda la iteración debería quedar un mensaje como el siguiente ejemplo
* howard_the_duck (H.W.) | M-10000001
* rocket_raccoon (R.R.) | NB-0000002
* wolverine (W.) |  M-10000003
* black_widow (B.W.) | F-20000004
………
Se asignaron ## códigos 
En donde ## es la cantidad de códigos que se generaron
La función deberá validar::
La lista contenga al menos un elemento
Todos los elementos de la lista sean del tipo diccionario

La función retornara la cadena generada si salió todo correctamente y False en caso de error

'''

def stark_generar_codigos_heroes(lista:list):
    contador = 0
    for heroe in lista:
        id_heroe_posicion = lista.index(heroe) +1
        codigo_heroe = generar_codigo_heroe(heroe,id_heroe_posicion)
        iniciales = extraer_iniciales(heroe['nombre'])
        nombre_formato = obtener_dato_formato(heroe['nombre'])
        print(f'* {nombre_formato} ({iniciales}) | {codigo_heroe}')
        contador += 1
    print(f'se asignaron {contador} codigos')
        

stark_generar_codigos_heroes(lista_personajes)

