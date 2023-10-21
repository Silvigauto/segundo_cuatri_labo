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

def validar_letras(lista_letras:list):
    letra = input('ingrese letra: ')
    while not letra.isalpha() or len(letra) != 1 or letra.upper() in lista_letras:
        letra = input('El caracter ingresado ya fue ingresado o no es valido')
    
    letra = letra.upper()
    return letra

                #arquero    []
def reemplazar_letras(palabra:str, lista_letras:list):
    abecedario = "abcdefghijklmnopqrstuvwxyz".upper() #convierto a mayuscula
    palabra_oculta = palabra #crea una variable 'palabra_oculta' y la asigna a la palabra a adivinar
    for letra in abecedario:
        if letra not in lista_letras:
                palabra_oculta = re.sub(letra, "_", palabra_oculta)
        else:
            pass
    return palabra_oculta #retorna la palabra con guiones(en la primera vuelta)

def ahorcado (temas:dict):
    jugando = True
    puntaje = 0
    vidas = 6

    while jugando:
        tema = obtener_tema(temas) #obtiene el tema
        palabra = obtener_palabra(temas,tema) #obtiene la palabra a adivinar
        lista_letras = []  #genera una lista vacia
        palabra_oculta = reemplazar_letras(palabra,lista_letras) # la palabra oculta con todos guiones |recibe la palabra a adivinar, lista letras vacia entonces reemplaza todo
        print(f"La categoria es:{tema} \n {palabra_oculta}") 
        print(f"Tu puntaje es: {puntaje}") #puntaje iniciado en 0


        while palabra != palabra_oculta:
            previa_palabra_oculta = palabra_oculta #crea variable 'previa_palabra_oculta' y le asigna la palbra con guiones
            letra_ingresada = validar_letras(lista_letras) # [] la funcion pide la letra, la valida y la devuelve
            lista_letras.append(letra_ingresada) #agrega la letra a la lista de letras
            palabra_oculta = reemplazar_letras(palabra,lista_letras) #vuelve a llamar a la funcion para reemplazar los guiones
                #palabra que se va adivinando| palabra con guiones   
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
            


ahorcado(diccionario_de_temas)
