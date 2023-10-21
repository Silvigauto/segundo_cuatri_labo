import re
import random
from datos import temas
from os import system
system('cls')

#elegir una tema del diccionario al azar
def generar_tema(diccionario_temas:dict):
    claves = list(diccionario_temas.keys())
    tema_elegido = random.choice(claves)
    return tema_elegido


#elegir un tema dentro de la lista de ese clave del diccionario
def generar_palabra(diccionario_temas:dict,clave:str):
    lista_temas = diccionario_temas[clave]
    posicion_aleatoria = random.randint(0, len(lista_temas)-1)
    palabra_oculta = lista_temas[posicion_aleatoria]
    palabra_oculta = palabra_oculta.upper()
    return palabra_oculta



def validar_letra(lista_letras):
    letra = input('Ingrese letra ').upper() 
    while letra.isalpha() == False or letra in lista_letras or len(letra) != 1:
        letra = input('Error: letra invalida o ya ingresada. Reingrese letra ').upper()

    return letra

def reemplazar_guiones(lista_letras,palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
    palabra_oculta = palabra #guardo en una variable para no perder la palabra original
    palabra_oculta = str(palabra_oculta)
    for letra in abecedario:
        if letra not in lista_letras:
            palabra_oculta = re.sub(letra, '_', palabra_oculta)
    
    return palabra_oculta

def ahorcado(diccionario_temas:dict):
    bandera_jugando = True
    vidas = 6
    puntaje = 0
    while bandera_jugando:
        tema = generar_tema(diccionario_temas)
        palabra = generar_palabra(diccionario_temas, tema)
        lista_letras = []
        palabra_oculta = reemplazar_guiones(lista_letras, palabra)
        print(f'La categoria es {tema}\n{palabra_oculta}')
        print(f'Vidas: {vidas} | Puntaje: {puntaje}')

        while palabra != palabra_oculta:
            previa_palabra_oculta = palabra_oculta
            letra = validar_letra(lista_letras)
            lista_letras.append(letra)
            palabra_oculta = reemplazar_guiones(lista_letras, palabra)
            
            if previa_palabra_oculta == palabra_oculta:
                vidas -= 1
                puntaje -= 10
            else:
                puntaje += 100

            print(palabra_oculta)
            print(f'Vidas: {vidas} | Puntaje: {puntaje}')

            if vidas == 0:
                bandera_jugando = False
                break
    print('Perdiste')









