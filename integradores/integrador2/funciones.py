#Silvina Gauto - 1B - Integrador 2 

from os import system
system('cls')

from data_stark import lista_personajes

#0
def stark_normalizar_datos(lista:list):
    bandera_datos_normalizados = False
    for heroe in lista:
        if type(heroe['fuerza']) != float:
            heroe['fuerza'] = float(heroe['fuerza'])
            bandera_datos_normalizados = True
        if type(heroe['altura']) != float:
            heroe['altura'] = float(heroe['altura'])
            bandera_datos_normalizados = True

        if type(heroe['peso']) != float:
            heroe['peso'] = float(heroe['peso'])
            bandera_datos_normalizados = True

    return bandera_datos_normalizados

#1.1
def obtener_dato(heroe:dict, clave:str):
    bandera_obtener_dato = False
    if len(heroe) > 0:
        if clave in heroe:
            bandera_obtener_dato = True
    
    return bandera_obtener_dato

#1.2
def obtener_nombre(heroe:dict):
    bandera_obtener_nombre = obtener_dato(heroe, 'hola')
    if bandera_obtener_nombre:
        return f"Nombre: {heroe['nombre']}"
    else:
        return bandera_obtener_nombre

#2
def obtener_nombre_y_dato(heroe:dict, clave:str):
    bandera_obtener_nombre = obtener_dato(heroe, clave)
    if bandera_obtener_nombre:
        return f"Nombre: {heroe['nombre']} | {clave}: {heroe[clave]}"
    else:
        return bandera_obtener_nombre

#3.1
def obtener_maximo(lista:list, clave:str):
    bandera_primero = True
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            if bandera_primero == True or heroe[clave] > maximo_dato:
                bandera_primero = False
                maximo_dato = heroe[clave]
        else:
            maximo_dato = False

    return maximo_dato

#3.2
def obtener_minimo(lista:list, clave:str):
    bandera_primero = True
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            if bandera_primero == True or heroe[clave] < minimo_dato:
                bandera_primero = False
                minimo_dato = heroe[clave]
        else:
            minimo_dato = False

    return minimo_dato

#3.3 obtener el numero de afuera ?
def obtener_dato_cantidad(lista:list, numero:int, clave:str):
    lista_coincidencias = []
    for heroe in lista:
        if heroe[clave] == numero:
            lista_coincidencias.append(heroe)
    return lista_coincidencias

#3.4 obtengo los datos de afuera para imprimir?
def stark_imprimir_heroes(lista):
    if len(lista) > 0:
        for heroe in lista:
            print(heroe)
    else:
        return False


#4.1
def sumar_dato_heroe(lista:list, clave:str):
    acumulador_clave = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) != 0:
            acumulador_clave += heroe[clave]
    
    return acumulador_clave

#4.2
def dividir(dividendo: float, divisor:int):
    if divisor != 0:
        resultado = dividendo/divisor
        return resultado
    else:
        return False
    

#4.3
def calcular_promedio(lista:list, clave:str):
    total_dato = sumar_dato_heroe(lista, clave)
    promedio = dividir(total_dato, len(lista))
    return promedio

'''
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una lista de héroes y un string que representa la clave del dato
Se debe validar que el dato que se encuentra en esa clave sea de tipo int o float. Caso contrario retornaria False
Se debe validar que la lista a manipular no esté vacía , en caso de que esté vacía se retornaria también False
'''

#4.4 --> falta validacion del tipo dato int o float

def mostrar_promedio_dato(lista:list, clave:str):
    if len(lista) > 0:
        if type(clave) == int or type(clave) == float:
            promedio = calcular_promedio(lista, clave)
            print(promedio)
        else:
            return False
    else:
        return False


def imprimir_menu():
    menu_opciones = ['1.Normalizar datos', 
                    '2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB', 
                    '3.Recorrer la lista y determinar cuál es el superhéroe más alto de género F', 
                    '4.Recorrer la lista y determinar cuál es el superhéroe más alto de género M',
                    '5.Recorrer la lista y determinar cuál es el superhéroe más débil de género M ',
                    '6.Recorrer la lista y determinar cuál es el superhéroe más débil de género NB',
                    '7.Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB',
                    '8.Determinar cuántos superhéroes tienen cada tipo de color de ojos.',
                    '9.Determinar cuántos superhéroes tienen cada tipo de color de pelo.',
                    '10.Listar todos los superhéroes agrupados por color de ojos.',
                    '11.Listar todos los superhéroes agrupados por tipo de inteligencia'
                    '12.salir']
    for opcion in menu_opciones:
        print(opcion)

#5.2
def validar_entero(numero:str):
    if numero.isdigit():
        return True
    else:
        return False

#5.3
def stark_menu_principal():
    imprimir_menu()
    opcion = input('Ingrese una opcion')
    opcion_usuario = validar_entero(opcion)

    if opcion_usuario:
        return int(opcion)
    else:
        return False


#################FUNCIONES PARA EL MENU#########################


##pensar con paramtetros opcionales el genero, default en todo, y si se especifica el genero que calcule en base a eso
#Recorrer la lista y determinar cuál es el superhéroe más alto de género F/M
def encontrar_maximo_clave_genero(lista:list, clave:str, genero:str):
    bandera_primero = True
    for heroe in lista:
        if heroe['genero'] == genero:
            if bandera_primero == True or heroe[clave] > maximo:
                maximo = heroe[clave]
                bandera_primero = False
    print(maximo)

#Recorrer la lista y determinar cuál es el superhéroe más débil de género M/NB
def encontrar_minimo_clave_genero(lista:list, clave:str, genero:str):
    bandera_primero = True
    for heroe in lista:
        if heroe['genero'] == genero:
            if bandera_primero == True or heroe[clave] < minimo:
                minimo = heroe[clave]
                bandera_primero = False
    print(minimo)

#Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB
def calcular_promedio_clave_genero(lista:list, clave:str, genero:str):
    contador_genero = 0
    acumulador = 0
    for heroe in lista:
        if heroe['genero'] == genero:
            acumulador += heroe[clave]
            contador_genero += 1
    promedio = acumulador/contador_genero
    print(promedio)

#Determinar cuántos superhéroes tienen cada tipo de color de ojos/color de pelo.
def setear_lista_clave(lista:list, clave:str):
    lista_tipos = []
    for heroe in lista:
        if clave in heroe:
            lista_tipos.append(heroe[clave])
    lista_tipos = set(lista_tipos)
    return lista_tipos

def contar_superheroes_por_categoria(lista:list,clave:str):
    lista_tipos = setear_lista_clave(lista,clave)
    for tipo in lista_tipos:
        contador = 0
        for heroe in lista:
            if heroe[clave] == tipo:
                contador += 1
        print(f'{tipo}: {contador}')

#Listar todos los superhéroes agrupados por color de ojos7inteligencia.
def listar_superheroes_por_categoria(lista:list,clave:str):
    lista_tipos = setear_lista_clave(lista, clave)
    for tipo in lista_tipos:
        print(tipo)
        for heroe in lista:
            if heroe[clave] == tipo:
                print(f"\t {heroe['nombre']}")


def stark_marvel_app(lista:list):

    bandera_opciones = False
    while True:
        opcion = stark_menu_principal()

        match opcion:
            case 1:
                datos_normalizados = stark_normalizar_datos(lista)
                if datos_normalizados:
                    print('datos normalizados')
                    bandera_opciones = True
                else:
                    print('Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')
            case 2:
                if bandera_opciones:
                    for heroe in lista:
                        if heroe['genero'] == 'NB':
                            print(obtener_nombre_y_dato(heroe, 'genero'))
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 3:
                if bandera_opciones:
                    encontrar_maximo_clave_genero(lista,'altura', 'F')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 4:
                if bandera_opciones:
                    encontrar_maximo_clave_genero(lista,'altura', 'M')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 5:
                if bandera_opciones:
                    encontrar_minimo_clave_genero(lista, 'fuerza', 'M')
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 6:
                if bandera_opciones:
                    encontrar_minimo_clave_genero(lista, 'fuerza', 'NB')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 7:
                if bandera_opciones:
                    calcular_promedio_clave_genero(lista, 'fuerza', 'NB')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 8:
                if bandera_opciones:
                    contar_superheroes_por_categoria(lista_personajes, 'color_ojos')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 9:
                if bandera_opciones:
                    contar_superheroes_por_categoria(lista_personajes, 'color_pelo')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 10:
                if bandera_opciones:
                    listar_superheroes_por_categoria(lista, 'color_ojos')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 11:
                if bandera_opciones:
                    listar_superheroes_por_categoria(lista, 'inteligencia')
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 12:
                break


