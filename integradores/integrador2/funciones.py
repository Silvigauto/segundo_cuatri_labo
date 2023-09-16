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
    menu_opciones = ['1.Normalizar datos', '2.otra opcion', '3.otra opcion', '4.otra opcion', '5.salir']
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
    

'''
6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
'''

def stark_marvel_app(lista:list):
    bandera_opciones = False
    while True:
        opcion = stark_menu_principal()

        match opcion:
            case 1:
                datos_normalizados = stark_normalizar_datos(lista_personajes)
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
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 4:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 5:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 6:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 7:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 8:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 9:
                if bandera_opciones:
                    pass
                else:
                    print('debe normalizar los datos primero, elija la opcion uno')
            case 10:
                break

