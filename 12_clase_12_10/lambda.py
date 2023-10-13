#objetos de primera clase
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

# def calcular(a,b, que_calcula):
#     resultado = que_calcula(a,b)
#     print(resultado)

# calcular(5,7, sumar)
# calcular(5,7, dividir)

#funciones lambda, no tiene nombre(son anonimas) no ocupan espacio en memoria------------------------------------------

# funcion = lambda a,b:(a+b)/2

# resultado = funcion(5,9)
# print(resultado)

########################

# def calcular(a,b, que_calcula):
#     resultado = que_calcula(a,b)
#     print(resultado)

# calcular(9,5, lambda a,b: (a+b)/2)


##MAP --> devuelve un objeto map

#vista algoritmica
# lista = [5,9,7,5,3,4,1,3,6,9,0,8]

# def duplicar(lista):
#     lista_modificada = []
#     for numero in lista:
#         x = numero*2
#         lista_modificada.append(x)
#     return lista_modificada

# lista_duplicada = duplicar(lista)



# lista_duplicada = list(map(lambda item: item*2,lista))
# print(lista_duplicada)


# colores = set(map(lambda heroe:heroe['color_ojos'], lista_personajes))

# for color in colores:
#     print(color)

##FILTER -> devuelve un objeto filter
#lista = [5,9,7,5,3,4,1,3,6,9,0,8]

#algoritmicamente
# pares = []
# for numero in lista:
#     if numero %2 == 0:
#         pares.append(numero)

# pares = list(filter(lambda numero:  numero %2 == 0, lista ))
# for numero in pares:
#     print(numero)


# from data_stark import *
# filtro = list(filter(lambda heroe:heroe['genero'] == 'M', lista_personajes))

# print(len(filtro))

##REDUCE --> recorre la lista, recibe dos parametros, anterior y actual, siempre devuelve el primer parametro
from functools import reduce

lista = [5,9,7,5,3,4,1,3,6,9,0,8]

# total = reduce(lambda anterior,actual:anterior + actual, lista, 0)

maximo = reduce(lambda max,actual: max if max>actual else actual, lista, 0 )
print(maximo)