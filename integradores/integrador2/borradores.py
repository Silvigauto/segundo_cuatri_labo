def calcular_promedio_clave_genero(lista:list, clave:str)->float:
    '''
    parameters: recibe la lista de géneros y la clave sobre la que se calculará el promedio
    brief: recorre la lista de géneros,acumula el valor de la clave pasada por parámetro y calcula el promedio
    return: retorna el promedio
    '''
    acumulador = 0
    for heroe in lista:
        acumulador += heroe[clave]
    promedio = acumulador/len(lista)
    return promedio