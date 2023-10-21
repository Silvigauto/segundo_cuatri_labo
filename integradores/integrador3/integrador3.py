
from os import system
system('cls')
import re
from data_stark import *


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



#2.1
def generar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    parameters: recibe el diccionario de un heroe y un id_heroe
    brief:genera el codigo del heroe pasado por parametro  'F-20000001 (10 caracteres)'
    return:retorna el codigo del heroe
            retorna'N/A' si no paso alguna validación
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


#2.2
def stark_generar_codigos_heroes(lista:list):
    '''
    parameters: recibe la lista de heroes
    brief: recorre la lista y genera el código de todos los heroes
            genera el id heroe(por posicion en la lista)
            valida que la lista contenga al menos un elemento
            que todos los elementos sea del tipo diccionario
    return: retorna la cadena generada
            retorna False en caso de error
    '''
    #cadena_generada = False
    contador = 0
    for heroe in lista:
        if type(heroe) == dict:
            id_heroe_posicion = lista.index(heroe) +1
            codigo_heroe = generar_codigo_heroe(heroe,id_heroe_posicion)
            iniciales = extraer_iniciales(heroe['nombre'])
            nombre_formato = obtener_dato_formato(heroe['nombre'])
            print(f'* {nombre_formato} ({iniciales}) | {codigo_heroe}')
            contador += 1
    print(f'se asignaron {contador} codigos')
    #return cadena_generada


#3.1
def sanitizar_entero(numero_str:str):
    '''
    parameters: recibe un string que representa el numero a sanitizar
    brief: analiza si el string es un numero entero positivo, quita los espacios de atras y adelante
    return: retorna el numero convertido a entero si este es positivo
            retorna -1 si contiene caracteres no numéricos
            retorna -2 si el número es negativo
            retorna -3 si es algun otro error
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




#3.2
def sanitizar_flotante(numero_str:str):
    '''
    parameters:recibe numero en formato string que hay que castear a flotante
    brief: analiza si el string recibido es un numero flotante positivo, quita los espacios en blanco de atras y adelante
    return: retorna el numero convertido a flotante si es positivo
            retorna -1 si contiene caracteres no numericos
            retorna -2 si es un numero negativo
            retorna -3 si ocurren otros problemas
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



def sanitizar_string(valor_str:str, valor_por_defecto = '-'):
    '''
    parameters: recibe 'valor_str' que representa el texto a validar
                recibe 'valor_por_defecto' parametro opcional
    brief: determina si el valor recibido es solo texto
            si encuentra una '/' la reemplaza por un espacio
            quita los espacios de atras y adelante
    return: retorna el texto convertido a minusculas
            si el valor_Str esta vacio retorna el valor por defecto convertido a minusculas
            retorna 'N/A' si contiene números
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



def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    '''
    parameters: recibe el diccionario del heroe
                recibe la clave a sanitizar
                reibe el tipo de dato a sanitizar 'entero'/'flotante'/'string'
    brief: sanitiza el valor recibido por parametro
            valida que 'tipo_dato' sea 'entero'/'flotante'/'string'
            valida que la clave si exista en el diccionario
    return: devuelve True en caso de haber sanitizado algun dato
            devuelve False en caso contrario
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




def stark_normalizar_datos(lista:list):
    '''
    parameters: recibe la lista de héroes
    brief: recorre la lista y sanitiza las claves : ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
            ‘inteligencia’
            valida que la lista no este vacia
    return: -
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





def stark_imprimir_indice_nombre(lista:list):
    '''
    parameters: recibe la lista de heroes
    brief: recorre la lista y muestra todos los nombres de los heroes separados por un guion
            si hay un 'the' lo ignora. howard-duck-rocket-raccoon-wolverine…
    return: no retorna nada
    '''
    for personaje in lista:
        nombre = re.sub(' the', '', personaje['nombre'])
        nombre = nombre.lower()
        nombre = re.split(' ', nombre)
        for palabra in nombre:
            print(palabra, end='-')



def generar_separador(patron:str, largo:int, imprimir = True):
    '''
    parameters: recibe un caracter con el que se realizara el separador
                recibe el largo que tendra el separador
                recibe un parametro opcional predeterminado en true (imprime y retorna o solo imprime)
    brief: genera el strin con el que patron y el largo recibido
            valida que el patron recibido tenga al menos un caracter y maximo dos
            valida que el largo sea un entero entre 1 y 235
    return: retorna el separador generado si el parametro 'imprimir' se encuentra en False
            retorna 'N/A' si no pasó alguna validación
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


def generar_encabezado(titulo:str):
    '''
    parameters: recibe el encabezado
    brief: convierte el titulo a letras mayusculas y envuelto en separadores
    return: retorna el encabezado formateado
    '''
    titulo = titulo.upper()
    separador = generar_separador('*', 158, False)

    encabezado = f'{separador}\n{titulo}\n{separador}'
    return encabezado


def imprimir_ficha_heroe(heroe:dict):
    '''
    parameters: recibe el diccionario del heroe
    brief: genera la ficha del heroe reutlizando funciones anteriores
    return: no retorna nada
    '''
    titulo_principal = generar_encabezado('principal')
    nombre = obtener_dato_formato(heroe['nombre'])
    iniciales = extraer_iniciales(heroe['nombre'])
    identidad = obtener_dato_formato(heroe['identidad'])
    consultora = obtener_dato_formato(heroe['empresa'])
    lista = lista_personajes
    id_heroe = (lista.index(heroe))+1
    codigo = generar_codigo_heroe(heroe, id_heroe)

    print(f"{titulo_principal}\nNOMBRE DEL HEROE: {nombre} ({iniciales})\nIDENTIDAD SECRETA: {identidad}\nCONSULTORA:{consultora}\nCÓDIGO DE HÉROE: {codigo}")

    titulo_fisico = generar_encabezado('fisico')
    altura = sanitizar_flotante(heroe['altura'])
    peso = sanitizar_flotante(heroe['peso'])
    fuerza = sanitizar_entero(heroe['fuerza'])
    
    print(f"{titulo_fisico}\nALTURA: {altura}cm.\nPESO: {peso}kg.\nFUERZA: {fuerza}N")

    titulo_señas_particulares= generar_encabezado('señas particulares')
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']
    print(f"{titulo_señas_particulares}\nCOLOR DE OJOS: {color_ojos}\nCOLOR DE PELO: {color_pelo}")




def stark_navegar_fichas(lista:list):
    '''
    parameters: recibe la lista de heroes
    brief: imprime la primer ficha del heroe y luego pide al usuario que ficha quiere imprimir (izq, der,salir)
            valida que no se ingrese cualquier valor
    return: no retorna nada
    '''
    posicion_heroe = 0
    imprimir_ficha_heroe(lista[posicion_heroe])
    while True:
        opcion = input('Ingrese ficha heroe:\n[ 1 ] Ir a la izquierda\n[ 2 ] Ir a la derecha\n[ 3 ] Salir ')
        match opcion:
            case '1':
                if posicion_heroe == 0:
                    posicion_heroe = 23
                else:
                    posicion_heroe -= 1                
                imprimir_ficha_heroe(lista[posicion_heroe])
            case '2':
                if posicion_heroe == 23:
                    posicion_heroe = 0
                else:
                    posicion_heroe += 1
                imprimir_ficha_heroe(lista[posicion_heroe])
            case '3':
                break
            case _:
                print('ingrese una opcion valida')

    print('has terminado de navegar las fichas')


def imprimir_menu():
    opciones = ['\n1 - Imprimir la lista de nombres junto con sus iniciales',
                '2 - Imprimir la lista de nombres y el código del mismo',
                '3 - Normalizar datos',
                '4 - Imprimir índice de nombres',
                '5 - Navegar fichas ',
                '6 - Salir\n']
    for opcion in opciones:
        print(opcion)

def validar_entero(numero:str)->bool:
    '''
    parameters: recibe un número en formato string
    brief: verifica que el string pasado por parámetro contenga solo números
    return: retorna True en caso que el string sea númerico
            retorna False en caso de que el string no sea enteramente numérico
    '''
    validacion = False
    if numero.isdigit():
        validacion = True

    return validacion

def stark_menu_principal()->int:
    '''
    parameters: no recibe parámetros
    brief: usa la función 'imprimir_menu', pide una opción al usuario y usa la función 'validar_entero' para verificar
            la opción ingresada
    return: retorna la opción convertida a entero
            retorna False en caso que la opción no fue validada
    '''
    imprimir_menu()
    opcion = input(f'\n\nIngrese una opcion')
    opcion_usuario = validar_entero(opcion)

    if opcion_usuario:
        opcion = int(opcion)
    else:
        opcion = False
    return opcion

