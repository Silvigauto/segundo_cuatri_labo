
import pygame

lista_mascotas = [
                {
                'nombre': 'pig', 
                'edad': 7, 
                'imagen': '4_clase_08_09\pig.jpg'
                },
                {
                'nombre':'perro',
                'edad':3,
                'imagen': '4_clase_08_09\perro.jpg'
                },
                {
                'nombre': 'gatito',
                'edad':1,
                'imagen': '4_clase_08_09\gatito.png'
                }]


CELESTE = (73,160,174)
ROJO = (255,0,0)
VERDE = (208,222,86)
GRIS = (96,96,96)

pygame.init()
VENTANA = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Mi primer ventana en pygame")

icono = pygame.image.load("2_clase_01_09\icono.png")
pygame.display.set_icon(icono)


VENTANA.fill(CELESTE)
fuente = pygame.font.SysFont("Arial", 30)#--> esto devuelve una superficie

flag = True
while flag == True:
    y = 50

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    for mascota in lista_mascotas:
        x = 50
        nombre = fuente.render(mascota['nombre'], False, GRIS, VERDE)
        edad = fuente.render(str(mascota['edad']), False, GRIS, VERDE  )
        imagen = pygame.image.load(mascota['imagen'])
        imagen = pygame.transform.scale(imagen, (90,90))

        VENTANA.blit(nombre, (x,y) )
        x += 100                    
        VENTANA.blit(edad, (x,y) )
        x += 100 
        VENTANA.blit(imagen, (x, y))
        y += 100
    
    

    pygame.display.update()

pygame.quit()