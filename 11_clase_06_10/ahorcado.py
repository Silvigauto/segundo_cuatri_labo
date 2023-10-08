from datos import diccionario_de_temas
import random
import re

def obtener_tema(temas: dict):
    claves = list(temas.keys())
    tema_aleatorio = random.choice(claves)
    return tema_aleatorio

def obtener_palabra(temas: dict, clave: str):
    lista_de_palabras = temas[clave]
    palabra = random.choice(lista_de_palabras)
    palabra = palabra.upper()
    return palabra

def validar_letras(lista_letras:list,letra:str):
    validacion = letra.isalpha() and letra.upper() not in (lista_letras)
    return validacion


def reemplazar_letras(palabra:str, lista_letras:list):
    abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
    palabra_oculta = palabra
    for letra in abecedario:
        if letra not in lista_letras:
                palabra_oculta = re.sub(letra, "_", palabra_oculta)
        else:
            pass
    return palabra_oculta

def ahorcado (temas:dict):
    jugando = True
    puntaje = 0
    vidas = 6

    while jugando:
        tema = obtener_tema(temas)
        palabra = obtener_palabra(temas,tema)
        lista_letras = []
        palabra_oculta = reemplazar_letras(palabra,lista_letras)
        print(f"La categoria es:{tema} \n {palabra_oculta}")
        print(f"Tu puntaje es: {puntaje}")


        while palabra != palabra_oculta:
            previa_palabra_oculta = palabra_oculta
            letra_ingresada = validar_letras(lista_letras)
            lista_letras.append(letra_ingresada)
            palabra_oculta = reemplazar_letras(palabra,lista_letras)
            if palabra_oculta == previa_palabra_oculta:
                vidas -= 1
                puntaje -= 5
                print(f"Te quedan {vidas} vidas")
            else:
                puntaje += 10

            if vidas == 0:
                jugando = False
                break
            
            print(palabra_oculta)
        

        puntaje += 100

    print(f"Tu puntaje final es: {puntaje}")
    print("juego finalizado")
            

