from configuraciones import *


figura_cuadrado =   {
            'tipo_figura':'cuadrado', 
            'color': ROSA, 
            'x': ancho/2-100, 
            'y':alto/2-150, 
            'ancho': 200, 
            'alto': 200
            }

figura_rectangulo =   {
            'tipo_figura':'rectangulo', 
            'color': AZUL_CLARO, 
            'x': ancho/2-200, 
            'y':alto/2-150, 
            'ancho': 400, 
            'alto': 200
            }


#recibe-->  el valor de x,y (punto centro del circulo) y el radio
figura_circulo =   {
            'tipo_figura':'circulo', 
            'color': VERDE, 
            'x': ancho/2, 
            'y':alto/2, 
            'radio': 110
            }




figura_triangulo =   {
            'tipo_figura':'triangulo', 
            'color': VERDE,
            #vertice izq  inf /vertice superior/ vertice der inf
            'puntos': [(150,370), (150,90), (370,370)]
            }