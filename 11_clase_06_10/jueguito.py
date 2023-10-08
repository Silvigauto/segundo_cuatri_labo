from ahorcado import*
from datos import diccionario_de_temas
import pygame

pygame.init()

BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

VENTANA = pygame.display.set_mode((800,800))

VENTANA.fill(BLANCO)

pygame.display.set_caption("AHORCADO")

fuente = pygame.font.SysFont("Arial",40)

def mostrar_texto(palabra:str,x:int,y:int):
    texto = fuente.render(palabra,False,NEGRO)
    VENTANA.blit(texto,(x,y))


palabra_adivinada = True
puntaje = 0
vidas = 6
jugando = True


while jugando:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill(BLANCO)

    if palabra_adivinada:
        tema = obtener_tema(diccionario_de_temas)
        palabra = obtener_palabra(diccionario_de_temas,tema)
        lista_letras = []
        palabra_oculta = reemplazar_letras(palabra,lista_letras)
        mensaje = (f"La categoria es:{tema} \n {palabra_oculta}")
        print(mensaje)
        mostrar_texto(mensaje,350,50)
        mensaje = (f"Tu puntaje es: {puntaje}")
        print(mensaje)
        mostrar_texto(mensaje,450,50)
        palabra_adivinada = False


    if palabra != palabra_oculta:
        VENTANA.fill(BLANCO)
        previa_palabra_oculta = palabra_oculta
        letra_ingresada = validar_letras(lista_letras)
        lista_letras.append(letra_ingresada)
        palabra_oculta = reemplazar_letras(palabra,lista_letras)
        if palabra_oculta == previa_palabra_oculta:
            vidas -= 1
            puntaje -= 5
            mensaje = (f"Te quedan {vidas} vidas")
            print(mensaje)
            mostrar_texto(mensaje,550,50)

        else:
            puntaje += 10

        if vidas == 0:
            jugando = False
            break
        
        mensaje = (f"{palabra_oculta}")
        print(mensaje)
        mostrar_texto(mensaje,650,50)
        
    else:
        palabra_adivinada = True
        puntaje += 100

        mensaje = f"Tu puntaje final es: {puntaje}"
        print(mensaje)
        mostrar_texto(mensaje,150,50)
        mensaje = ("Juego finalizado")
        print(mensaje)
        mostrar_texto(mensaje,250,50)

    pygame.display.update()

pygame.quit()
