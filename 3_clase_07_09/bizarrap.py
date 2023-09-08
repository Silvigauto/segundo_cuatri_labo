from os import system
system('cls')

from data import lista_bzrp

'''
{
    'title': 'QUEVEDO || BZRP Music Sessions #52', 
    'views': 227192970, 
    'length': 204, 
    'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
    'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
    'date': '2022-07-06 00:00:00'
}
'''


while True:
    respuesta = int(input("1.Tema mas visto\n2.Duracion Promedio\n3.Cantidad de temas sobre el promedio\n4.Salir\nElija una opcion:"))
    match respuesta:
        case 1:
            bandera_primero = False
            maximo_vistas = 0
            for video in lista_bzrp:
                vistas = video['views']
                if bandera_primero == False or vistas > maximo_vistas:
                    maximo_vistas = vistas
                    bandera_primero = True

            print(maximo_vistas)

            for video in lista_bzrp:
                vistas = video['views']
                titulo = video['title']
                if vistas == maximo_vistas:
                    print(titulo)
        case 2:
            #tiempo promedio 
            acumulador = 0
            for video in lista_bzrp:
                duracion = video['length']
                acumulador += duracion

            promedio = acumulador/len(lista_bzrp)
            print(promedio)
        case 3:
            #temas que superan el promedio
            acumulador = 0
            for video in lista_bzrp:
                duracion = video['length']
                acumulador += duracion

            promedio = acumulador/len(lista_bzrp)
            
            for video in lista_bzrp:
                duracion = video['length']
                nombre = video['title']

                if duracion > promedio:
                    print(nombre)
        case 4:
            break
