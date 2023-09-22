'''
Ejercicios Funciones

Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.

Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista con las palabras ordenadas alfabéticamente.

Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.

Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de todos los elementos.

Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de ellas mediante un menú de opciones.

'''
import math
pi = math.pi

#Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def calcular_area_circulo(radio:int):
    if type(radio) == int:
        area = pi * radio ** 2
    else: 
        area = False
    
    return area

#Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def verificar_par_impar(numero:int):
    if type(numero) == int:
        if numero % 2 == 0:
            print('el numero es par')
        else:
            print('el numero es impar')
    else:
        print('no es un numero entero')

#Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.
def sumar_numeros_listas(lista:list):
    if type(lista) == list and len(lista) > 0:
        acumulador = 0
        for numero in lista:
            if type(numero) == int or type(numero) == float:
                acumulador += numero
        return acumulador
    else:
        print('error con la lista')

#Ejercicio 04: Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo(primer_numero:int, segundo_numero:int, tercer_numero:int):
    lista_numeros = []
    bandera_primero = True
    if type(primer_numero) == int and  type(segundo_numero) == int and  type(tercer_numero) == int:
        lista_numeros.extend([primer_numero, segundo_numero, tercer_numero])
        for numero in lista_numeros:
            if bandera_primero == True or numero > numero_maximo:
                numero_maximo = numero
                bandera_primero = False
        return numero_maximo

    else:
        return False

#Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.