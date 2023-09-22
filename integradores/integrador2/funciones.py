#Silvina Gauto - 1B - Integrador 2 

#0
def stark_normalizar_datos(lista:list)->bool:
    '''
    parameters: recibe la lista de héroes
    brief: normaliza los datos numéricos en la lista de héroes
    return: retorna False si ya se han normalizado los datos o si no se pudo realizar
            retorna True si al menos un dato fue normalizado
    '''
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
def obtener_dato(heroe:dict, clave:str)->bool:
    '''
    parameters: recibe un diccionario y una clave de este
    brief: valida si el diccionario está vacio y si la clave existe en el diccionario
    return: retorna True si no es un diccionario vacío y si la clave existe en este
            retorna False en caso contrario
    '''
    bandera_obtener_dato = False
    if len(heroe) > 0:
        #if 'nombre' in heroe
        if clave in heroe:
            bandera_obtener_dato = True
    
    return bandera_obtener_dato


#1.2
def obtener_nombre(heroe:dict)->str:
    '''
    parameters: recibe un diccionario que representa al héroe
    brief: en base a la función 'obtener_dato' (para validar si el diccionario no está vacio) y si existe la clave 'nombre'
        formatea el nombre del héroe
    return: retorna el nombre del héroe si pasó las validaciones
            retorna False en caso contrario
    '''
    bandera_obtener_nombre = obtener_dato(heroe, 'hola')
    if bandera_obtener_nombre:
        return f"Nombre: {heroe['nombre']}"
    else:
        return bandera_obtener_nombre


#2
def obtener_nombre_y_dato(heroe:dict, clave:str)->str:
    '''
    parameters: recibe un diccionario que representa el héroe y su clave
    brief: en base a 'obtener_dato' (valida si el diccionario no esta vacio y si existe la clave) formatea el string con el nombre y la clave pasada
        por parámetro
    return: retorna el string formateado
            retorna False en caso de no pasar las validaciones
    '''
    bandera_obtener_nombre = obtener_dato(heroe, clave)
    if bandera_obtener_nombre:
        return f"Nombre: {heroe['nombre']} | {clave}: {heroe[clave]}"
    else:
        return bandera_obtener_nombre

#3.1
def obtener_maximo(lista:list, clave:str)->float:
    '''
    parameters: recibe la lista de héroes y una clave del diccionario
    brief: recorre la lista y obtiene el numero máximo de la clave pasada por parámetro
    return: retorna el máximo dato 
            retorna False si la clave pasada no es de tipo numérico
    '''
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
def obtener_minimo(lista:list, clave:str)->float:
    '''
    parameters: recibe la lista de héroes y una clave del diccionario   
    brief: recorre la lista y obtiene el número mínimo de la clave pasada por parámetro
    return: retorna el mínimo dato  
            retorna False si la clave pasada no es de tipo numérico
    '''
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
def obtener_dato_cantidad(lista:list, numero:int, clave:str)->list:
    '''
    parameters: recibe la lista de héroes, el número máximo o mínimo a encontrar, recibe la clave del héroe
    brief: recorre la lista de héroes y agrega a una lista los diccionarios que coincidan con el máximo o el mínimo
    return: retorna la lista de coincidencias
    '''
    lista_coincidencias = []
    for heroe in lista:
        if heroe[clave] == numero:
            lista_coincidencias.append(heroe)
    return lista_coincidencias

#3.4 obtengo los datos de afuera para imprimir?
def stark_imprimir_heroes(lista)->bool:
    '''
    parameters: recibe la lista de héroes   
    brief: recorre la lista (si no está vacía) e imprime todos los héroes
    return: retorna False si la lista está vacía
    '''
    if len(lista) > 0:
        for heroe in lista:
            print(heroe)
    else:
        return False


#4.1
def sumar_dato_heroe(lista:list, clave:str)->float:
    '''
    parameters: recibe la lista de héroes y la clave a sumar
    brief: recorre la lista de héroes y suma todos los datos de la clave pasada por parámetro
    return: retorna el acumulador final
    '''
    acumulador_clave = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) != 0:
            acumulador_clave += heroe[clave]
    
    return acumulador_clave

#4.2
def dividir(dividendo: float, divisor:int)->float:
    '''
    parameters: recibe el número a divivir y el divisor
    brief: realiza la división de los números pasados por parámetro
    return: retorna el resultado de la división
            retorna False en caso que el divisor sea 0
    '''
    if divisor != 0:
        resultado = dividendo/divisor
        return resultado
    else:
        return False
    

#4.3
def calcular_promedio(lista:list, clave:str)->float:
    '''
    parameters: recibe la lista de héroes y la clave sobre la que se va a calcular el promedio
    brief: toma el acumulador de la función 'sumar_dato_heroe' y el largo de la lista como divisor y dividendo
            de la función 'dividir'
    return: retorna el promedio
    '''
    total_dato = sumar_dato_heroe(lista, clave)
    promedio = dividir(total_dato, len(lista))
    return promedio

'''
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una lista de héroes y un string que representa la clave del dato
Se debe validar que el dato que se encuentra en esa clave sea de tipo int o float. Caso contrario retornaria False
Se debe validar que la lista a manipular no esté vacía , en caso de que esté vacía se retornaria también False
'''

#4.4 --> falta validacion del tipo dato int o float
def mostrar_promedio_dato1(lista:list, clave:str):
    '''
    parameters: 
    brief: 
    return: 
    '''
    if len(lista) > 0:
        for heroe in lista:
            if type(heroe[clave]) == int or type(heroe[clave]) == float:
                pass
            else:
                return False
    else:
        return False

def mostrar_promedio_dato(lista:list, clave:str):
    '''
    parameters: 
    brief: 
    return: 
    '''
    if len(lista) > 0:
        if type(clave) == int or type(clave) == float:
            promedio = calcular_promedio(lista, clave)
            print(promedio)
        else:
            return False
    else:
        return False

#pasar el menu por parámetro????

def imprimir_menu()->None:
    '''
    parameters: no recibe parámetros
    brief: recorre el menu_opciones e imprime cada opción
    return: no retorna nada
    '''
    menu_opciones = ['\n1.Normalizar datos', 
                    '2.imprimir el nombre de cada superhéroe NB', 
                    '3.héroe más alto F', 
                    '4.héroe más alto M',
                    '5.héroe más débil M ',
                    '6.héroe más débil NB',
                    '7.fuerza promedio héroes NB',
                    '8.cuántos héroes tienen cada tipo de color de ojos.',
                    '9.cuántos héroes tienen cada tipo de color de pelo.',
                    '10.Listar héroes agrupados por color de ojos.',
                    '11.Listar héroes agrupados por tipo de inteligencia',
                    '12.salir']
    for opcion in menu_opciones:
        print(opcion)

#5.2
def validar_entero(numero:str)->bool:
    '''
    parameters: recibe un número en formato string
    brief: verifica que el string pasado por parámetro contenga solo números
    return: retorna True en caso que el string sea númerico
            retorna False en caso de que el string no sea enteramente numérico
    '''
    if numero.isdigit():
        return True
    else:
        return False

#5.3
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
        return int(opcion)
    else:
        return False


#################FUNCIONES PARA EL MENU#########################

#generar una lista que retorne otra lista con los heroes por genero
def obtener_superheroes_por_genero(lista:list, genero:str)->list:
    '''
    parameters: recibe la lista de héroes, y un string que representa el genero 'F'/'M'/'NB'
    brief: recorre la lista de héroes y si es del género pasado por parámetro lo agrega a una lista
    return: retorna la lista de géneros
    '''
    lista_generos = []
    for heroe in lista:
        if heroe['genero'] == genero:
            lista_generos.append(heroe)
    return lista_generos

#Determinar cuántos superhéroes tienen cada tipo de color de ojos/color de pelo.
def setear_lista_clave(lista:list, clave:str)->list:
    '''
    parameters: recibe la lista de héroes y la clave sobre la que se va a generar una lista
    brief: recorre la lista de héroes y genera una lista seteada con todas las keys de la clave pasada por parámetro
    return: retorna la lista seteada
    '''
    lista_tipos = []
    for heroe in lista:
        if clave in heroe:
            lista_tipos.append(heroe[clave])
    lista_tipos = set(lista_tipos)
    return lista_tipos


def contar_superheroes_por_categoria(lista:list,clave:str)->None:
    '''
    parameters: recibe la lista de héroes y y la clave sobre la que se va a contar 
    brief: recorre lista_tipos de 'setear_lista_clave' y por cada tipo recorre la lista de heroes y si coincide lo cuenta
            e imprime el contador
    return: nada
    '''
    lista_tipos = setear_lista_clave(lista,clave)
    for tipo in lista_tipos:
        contador = 0
        for heroe in lista:
            if heroe[clave] == tipo:
                if tipo == '':
                    tipo = 'no tiene'
                    contador +=1
                else:
                    contador += 1

        print(f'{tipo}: {contador}')

#Listar todos los superhéroes agrupados por color de ojos/inteligencia.
def listar_superheroes_por_categoria(lista:list,clave:str)->None:
    '''
    parameters: recibe la lista de héroes y la clave sobre la que se va a contar
    brief: recorre lista_tipos de 'setear_lista_clave' y por cada tipo recorre la lista de héroes y si coincide muestra el nombre
    return: nada
    '''
    lista_tipos = setear_lista_clave(lista, clave)
    for tipo in lista_tipos:
        if tipo == '':
            print('no tiene')
        else:
            print(tipo)
        for heroe in lista:
            if heroe[clave] == tipo:
                print(f"\t {heroe['nombre']}")





