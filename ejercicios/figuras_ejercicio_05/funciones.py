
from diccionarios_figuras import * #--> de aca viene el pygame, el pi etc

#-------------------FUNCIONES------------------------------------
#PERIMETROS
def calcular_perimetro_cuadrado(figura:dict):
    perimetro = figura['ancho'] * 4
    return perimetro

def calcular_perimetro_rectangulo(figura:dict):
    perimetro = 2 * (figura['ancho'] + figura['alto'])
    return perimetro


def calcular_perimetro_circulo(figura:dict):
    circunferencia = 2 * pi * figura['radio']
    return circunferencia

def calcular_perimetro_triangulo(figura:dict):
    #vertice izq  inf /vertice superior/ vertice der inf
    #'puntos': [(150,370), (150,90), (370,370)]
    #                   y1                y2
    altura = figura['puntos'][0][1] - figura['puntos'][1][1]
    #                   x3              x1
    base = figura['puntos'][2][0] - figura['puntos'][0][0]

    coordenada_hipotenusa_A = figura['puntos'][2][0] - figura['puntos'][1][0] #x3-x2
    coordenada_hipotenusa_C = figura['puntos'][2][1] - figura['puntos'][1][1] #y3-y2
    hipotenusa = ((coordenada_hipotenusa_A ** 2) + (coordenada_hipotenusa_C ** 2)) ** 0.5
    
    perimetro = altura + base + hipotenusa

    return perimetro

#AREAS
def calcular_area_cuadrado(figura:dict):
    area = figura['ancho'] * figura['ancho']
    return area

def calcular_area_rectangulo(figura:dict):
    area = figura['ancho'] * figura['alto']
    return area


def calcular_area_circulo(figura:dict):
    area = (pi * figura['radio']) ** 2
    return area


def calcular_area_triangulo(figura:dict):
    #x3 - x1
    base = figura['puntos'][2][0] - figura['puntos'][0][0]
    altura = figura['puntos'][0][1] - figura['puntos'][1][1]
    area = (base*altura) / 2
    return area


#CALCULOS
##match no anda D:


def calcular_perimetro_figura(figura:dict):
    if figura == figura_cuadrado:
        perimetro = calcular_perimetro_cuadrado(figura)
    elif figura == figura_rectangulo:
        perimetro = calcular_perimetro_rectangulo(figura)
    elif figura == figura_circulo:
        perimetro = calcular_perimetro_circulo(figura)
    else:
        perimetro = calcular_perimetro_triangulo(figura)
    return perimetro

def calcular_area_figura(figura:dict):
    if figura == figura_cuadrado:
        area = calcular_area_cuadrado(figura)
    elif figura == figura_rectangulo:
        area = calcular_area_rectangulo(figura)
    elif figura == figura_circulo:
        area = calcular_area_circulo(figura)
    else:
        area = calcular_area_triangulo(figura)
    return area

#-------------FUNCIONES FINALES------------------


def dibujar_figura_ventana(figura:dict):
    if figura == figura_circulo:
        pygame.draw.circle(PANTALLA, figura['color'], (figura['x'], figura['y']), figura['radio'])
    elif figura == figura_triangulo:
        pygame.draw.polygon(PANTALLA, figura['color'], figura['puntos'])
    else:
        pygame.draw.rect(PANTALLA, figura['color'], (figura['x'], figura['y'], figura['ancho'], figura['alto'] ))

def mostrar_resultados_ventana(figura:dict):
    perimetro = calcular_perimetro_figura(figura)
    area = calcular_area_figura(figura)

    resultado_perimetro_figura = fuente.render(f"Perimetro {figura['tipo_figura']}: {str( perimetro)}", False, BLANCO, AZUL)
    resultado_area_figura = fuente.render(f"Area {figura['tipo_figura']}: {str(area)}", False, BLANCO, AZUL)

    PANTALLA.blit(resultado_perimetro_figura, (50, 420))
    PANTALLA.blit(resultado_area_figura, (50, 450))

def dibujar_y_mostrar_resultado_figura(figura:dict):
    dibujar_figura_ventana(figura)
    mostrar_resultados_ventana(figura)
