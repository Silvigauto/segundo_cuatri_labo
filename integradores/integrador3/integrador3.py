
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
    '''
    parameters: recibe el nombre del heroe
    brief: genera un string con las iniciales del heroe
            valida que el string recibido no este vacío
    return: devuelve el string generado con las iniciales
            devuelve 'N/A' si no paso las validaciones
    '''
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
    '''
    parameters: recibe un string que representa un dato
    brief:convierte al dato con _  por ejemplo: Howard the Duck -> howard_the_duck
        valida que el dato recibido sea del tipo str
    return: retorna el nombre con el formato especificada
            retorna false si no paso alguna validacion
    '''
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
    '''
    parameters: recibe el diccionario del heroe
    brief: imprime con el siguiente formato  * howard_the_duck (H.W.)
            valida que el dato recibido sea de tipo diccionario
            que el diccionario contenga la clave nombre
    return: retorna True en caso de haber finalizado con exito
            retorna False si no paso alguna validación
    '''
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
    '''
    parameters: recibe la lista de héroes
    brief: utliza 'stark_imprimir_nombre_con_iniciales' para recorrer la lista e imprimir todos los nombres
            valida que que el parametro sea de tipo lista
            valida que la la lista contenga al menos un elemento
    return: retorna True si se pudieron imprimirse todos los nombres
            retorna False si no paso alguna validacion
    '''
    finalizacion = False
    if type(lista) == list and len(lista) != 0:
        for heroe in lista:
            stark_imprimir_nombre_con_iniciales(heroe)
        finalizacion = True

    return finalizacion


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
    '''
    parameters: recibe el diccionario de un heroe y un id_heroe
    brief:genera el codigo del heroe pasado por parametro  'F-20000001 (10 caracteres)'
    return:
    '''
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
#2.2
def stark_generar_codigos_heroes(lista:list):
    '''
    parameters:
    brief:
    return:
    '''
    cadena_generada = False
    contador = 0
    for heroe in lista:
        if type(heroe) == dict:
            id_heroe_posicion = lista.index(heroe) +1
            codigo_heroe = generar_codigo_heroe(heroe,id_heroe_posicion)
            iniciales = extraer_iniciales(heroe['nombre'])
            nombre_formato = obtener_dato_formato(heroe['nombre'])
            cadena_generada = f'* {nombre_formato} ({iniciales}) | {codigo_heroe}'
            contador += 1
    print(f'se asignaron {contador} codigos')
    return cadena_generada
        
'''
Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
numero_str: un string que representa un posible número entero
La función deberá analizar el string recibido y determinar si es un número entero positivo.  La función debe devolver distintos valores según el problema encontrado:
Si contiene carácteres no numéricos retornar -1
Si el número es negativo se deberá retornar un -2
Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número entero positivo, retornarlo convertido en entero

'''
#3.1
def sanitizar_entero(numero_str:str):
    '''
    parameters:
    brief:
    return:
    '''
    numero = numero_str.strip()
    if numero[0] == '-':
        numero = -2
    elif numero_str.isdigit():
        numero = int(numero_str)
    elif numero_str.isdigit() == False:
        numero = -1
    else:
        numero = -3
    
    return numero



'''

Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
numero_str: un string que representa un posible número decimal
La función deberá analizar el string recibido y determinar si es un número flotante positivo.  La función debe devolver distintos valores según el problema encontrado:
Si contiene carácteres no numéricos retornar -1
Si el número es negativo se deberá retornar un -2
Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número flotante positivo, retornarlo convertido en flotante
'''
#3.2
def sanitizar_flotante(numero_str:str):
    '''
    parameters:
    brief:
    return:
    '''
    numero = numero_str.strip()
    if numero[0] == '-':
        numero = -2
    elif '.' in numero or numero.isdigit():
        numero = float(numero_str)
    elif numero.isdigit() == False:
        numero = -1
    else:
        numero = -3

    return numero

'''
Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
valor_str: un string que representa el texto a validar
valor_por_defecto: un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)

La función deberá analizar el string recibido y determinar si es solo texto (sin números). En caso de encontrarse números retornar “N/A”

En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio

El espacio es un caracter válido 

En caso que se verifique que el parámetro recibido es solo texto, se deberá retornar el mismo convertido todo a minúsculas

En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, entonces retornar el valor por defecto convertido a minúsculas

Quitar los espacios en blanco de atras y adelante de ambos parámetros en caso que los tuviese
'''

#3.3 --> FALTA VALIDAR '253 HOLA' NUMEROS

def sanitizar_string(valor_str:str, valor_por_defecto = '-'):
    '''
    parameters:
    brief:
    return:
    '''
    bandera_espacio = False
    valor_str = re.sub('/', ' ', valor_str)

    
    if len(valor_str) > 0:
        if valor_str.isalpha():
            valor_str = valor_str.lower()
        else:
            for caracter in valor_str:
                if caracter == ' ':
                    bandera_espacio = True
            if bandera_espacio:
                valor_str = valor_str.lower()
            else:
                valor_str = 'N/A'
    else:
        valor_str = valor_por_defecto.lower()

    valor_str = valor_str.strip()

    return valor_str


'''
3.4. Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
● heroe: un diccionario con los datos del personaje
● clave: un string que representa el dato a sanitizar (la clave del
diccionario). Por ejemplo altura
● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
tomar los valores: ‘string’, ‘entero’ y ‘flotante’
La función deberá sanitizar el valor del diccionario correspondiente a la clave
y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los
puntos 3.1, 3.2, 3.3 
Se deberá validar:
● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
minúsculas. En caso de encontrarse un valor no válido informar por
pantalla: ‘Tipo de dato no reconocido’

● Que clave exista como clave dentro del diccionario heroe. En caso de
no encontrarse, informar por pantalla: ‘La clave especificada no
existe en el héroe’. (en este caso la validación es sensible a
mayúsculas o minúsculas)
Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y
False en caso contrario.
'''

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    '''
    parameters:
    brief:
    return:
    '''
    bandera_normalizacion = False
    bandera_existe_clave = False

    tipo_dato = tipo_dato.lower()

    if tipo_dato == 'string' or tipo_dato == 'flotante' or tipo_dato == 'entero':
        for key in heroe:
            if key == clave:
                bandera_existe_clave = True
        if bandera_existe_clave:
            match tipo_dato:
                case 'string':
                    heroe[clave] = sanitizar_string(heroe[clave])
                    if heroe[clave]  != 'N/A':
                        bandera_normalizacion = True
                case 'flotante':
                    heroe[clave] = sanitizar_flotante(heroe[clave])
                    if type(heroe[clave]) == float:
                        bandera_normalizacion = True
                case 'entero':
                    heroe[clave] = sanitizar_entero(heroe[clave])
                    if heroe[clave]  != -1 and heroe[clave]   != -2 and heroe[clave]   != -3 :
                        bandera_normalizacion = True
        else:
            print('la clave especificada no existe en el diccionario')

    else:
        print('Tipo de dato no reconocido')
    
    return bandera_normalizacion


'''
3.5. Actualizar la función 'stark_normalizar_datos’ usando las funciones de
sanitizar.
La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
‘inteligencia’
● Validar que la lista de héroes no esté vacía para realizar sus acciones,
caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
● Reutilizar la función sanitizar_dato
'''

def stark_normalizar_datos(lista:list):
    '''
    parameters:
    brief:
    return:
    '''
    if len(lista) !=0:
        for heroe in lista:
            for clave in heroe:
                if clave == 'altura':
                    sanitizar_dato(heroe, clave, 'flotante')
                if clave == 'peso':
                    sanitizar_dato(heroe, clave, 'flotante')
                if clave == 'color_ojos':
                    sanitizar_dato(heroe, clave, 'string')
                if clave == 'color_pelo':
                    if heroe[clave] == '':
                        heroe[clave] = re.sub('', 'no tiene', heroe[clave])
                    sanitizar_dato(heroe, clave, 'string')
                if clave == 'fuerza':
                    sanitizar_dato(heroe, clave, 'entero')
                if clave == 'inteligencia':
                    if heroe[clave] == '':
                        heroe[clave] = re.sub('', 'no tiene', heroe[clave])
                    sanitizar_dato(heroe, clave, 'string')
    else:
        print('error, lista de heroes vacia')



'''
4.1. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
parámetro:
● lista_heroes: la lista de personajes
La función deberá mostrar por pantalla cada una de las palabras (en
minúscula) de cada uno de los nombres que existan en el data_stark
separado por un guión entre cada una de las palabras ignorando las palabras
que contengan “the” --> (Usar regex para separar esto)

Por ejemplo:
howard-duck-rocket-raccoon-wolverine…
'''

def stark_imprimir_indice_nombre(lista:list):
    '''
    parameters:
    brief:
    return:
    '''
    for personaje in lista:
        nombre = re.sub(' the', '', personaje['nombre'])
        nombre = nombre.lower()
        nombre = re.split(' ', nombre)
        for palabra in nombre:
            print(palabra, end='-')

'''
5.1 Crear la función ‘generar_separador’ la cual recibirá como parámetro

● patron: un carácter que se utilizará como patrón para generar el
separador
● largo: un número que representa la cantidad de caracteres que va
ocupar el separador.
● imprimir: un parámetro opcional del tipo booleano (por default definir
en True)
La función deberá generar un string que contenga el patrón especificado
repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
al otro, sin salto de línea)

Si el parámetro booleano recibido se encuentra en False se deberá solo
retornar el separador generado. Si se encuentra en True antes de retornarlo,
imprimirlo por pantalla
La función deberá validar:
● Que el parámetro patrón tenga al menos un carácter y como máximo
dos
● Que el parámetro largo sea un entero entre 1 y 235 inclusive
En caso de no verificarse las validaciones devolver ‘N/A’

Ejemplo de llamada:
generar_separador(‘*’, 10)
Ejemplo de salida:
**********
'''

def generar_separador(patron:str, largo:int, imprimir = True):
    '''
    parameters:
    brief:
    return:
    '''
    cadena = 'N/A'
    if len(patron) > 0 and len(patron) <= 2:
        if largo > 0 and largo <= 235:
            cadena = ''
            for i in range(largo):
                cadena += patron
    if imprimir:
        print(cadena)
    
    return cadena

'''
5.2 Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
● titulo: un string que representa el título de una sección de la ficha
La función deberá devolver un string que contenga el título envuelto entre dos
separadores (estimar el largo requerido para tu pantalla).
Ejemplo de salida:
********************************************************************************
PRINCIPAL
********************************************************************************
La función deberá convertir el título recibido en todas letras mayúsculas
'''

def generar_encabezado(titulo:str):
    '''
    parameters:
    brief:
    return:
    '''
    titulo = titulo.upper()
    separador = generar_separador('*', 158, False)

    print(f'{separador}\n{titulo}\n{separador}')

'''
5.3 Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:

● heroe: un diccionario con los datos del héroe
La función deberá a partir los datos del héroe generar un string con el
siguiente formato e imprimirlo por pantalla::
***************************************************************************************
PRINCIPAL
***************************************************************************************
NOMBRE DEL HÉROE: spider_man (S.M.)
IDENTIDAD SECRETA: peter_parker
CONSULTORA: marvel_comics
CÓDIGO DE HÉROE : M-10000001
***************************************************************************************
FISICO

***************************************************************************************
ALTURA: 178 cm.
PESO: 74,25 kg.
FUERZA: 55 N
***************************************************************************************
SEÑAS PARTICULARES
***************************************************************************************
COLOR DE OJOS: Hazel
COLOR DE PELO: Brown
'''

##PENDIENTES --> CODIGO HEROE, FORMATO FUERZA PESO ALTURA
def imprimir_ficha_heroe(heroe:dict):
    '''
    parameters:
    brief:
    return:
    '''
    generar_encabezado('principal')
    nombre = obtener_dato_formato(heroe['nombre'])
    iniciales = extraer_iniciales(heroe['nombre'])
    identidad = obtener_dato_formato(heroe['identidad'])
    consultora = obtener_dato_formato(heroe['empresa'])

    codigo = generar_codigo_heroe(heroe, 1)
    print(f"NOMBRE DEL HEROE: {nombre} ({iniciales})\nIDENTIDAD SECRETA: {identidad}\nCONSULTORA:{consultora}\nCÓDIGO DE HÉROE: {codigo}")

    generar_encabezado('fisico')
    altura = heroe['altura']
    peso = heroe['peso']
    fuerza = heroe['fuerza']
    print(f"ALTURA: {altura}\nPESO: {peso}\nFUERZA: {fuerza}")

    generar_encabezado('señas particulares')
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']
    print(f"COLOR DE OJOS: {color_ojos}\nCOLOR DE PELO: {color_pelo}")

'''
5.4 Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
lista_heroes: la listas personajes
La función deberá comenzar imprimiendo la ficha del primer personaje de la lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
[ 1 ] Ir a la izquierda 		[ 2 ] Ir a la derecha 		[ 3 ] Salir
Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en la posición anterior en la lista  (en caso de estar en el primero, ir al último)


Si el usuario ingresa ‘2’:  se debe mostrar el héroe que se encuentra en la posición siguiente en la lista (en caso de estar en el último, ir al primero)


Si ingresa 3: volver al menú principal


Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que ingrese un valor válido
Recordatorio: Se pueden usar índices negativos si desean
'''


def stark_navegar_fichas(lista:list):
    '''
    parameters:
    brief:
    return:
    '''
    posicion_heroe = 0
    imprimir_ficha_heroe(lista[posicion_heroe])
    while True:
        opcion = int(input('Ingrese ficha heroe:\n[ 1 ] Ir a la izquierda\n[ 2 ] Ir a la derecha\n[ 3 ] Salir '))
        match opcion:
            case 1:
                if posicion_heroe == 0:
                    posicion_heroe = 23
                else:
                    posicion_heroe -= 1                
                imprimir_ficha_heroe(lista[posicion_heroe])
            case 2:
                if posicion_heroe == 23:
                    posicion_heroe = 0
                else:
                    posicion_heroe += 1
                imprimir_ficha_heroe(lista[posicion_heroe])
            case 3:
                break

    print('has terminado de navegar las fichas')

#stark_navegar_fichas(lista_personajes)