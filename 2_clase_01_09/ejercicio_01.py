from os import system
system('cls')
'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo
desarrollo en python,
que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
    # Inteligencia artificial (IA),
    # Realidad virtual/aumentada (RV/RA),
    # Internet de las cosas (IOT) o
    # Procesamiento de lenguaje natural (NLP).


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:


A) Los datos a ingresar por cada empleado encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
    50 años inclusive.
    2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
    Femenino o su edad se encuentre entre los 33 y 40.
    3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    de ese género.
'''


lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 49, 27]

lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
                        "Otro", "Femenino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
                        "Femenino", "Masculino", "Otro"]


lista_tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP",
                    "RV/RA", "RV/RA", "NLP", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]  


contador = 0
contador_ia = 0
bandera = False
lista_maxima_edad = []

for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    #justifcado 15 caracteres ?)
    print(f"{nombre:15} {edad}\t{genero:15}{tecnologia}")

# 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    if genero == 'Masculino':
        if (tecnologia == 'IOT' or tecnologia == 'IA'):
            if (edad >= 25 and edad <=50):
                contador += 1

#2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
    if tecnologia != 'IA' and (genero != 'Femenino' or (edad >=33 and edad <= 40)):
        contador_ia += 1

#3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
#de ese género.
    if genero == 'Masculino':
        if bandera == False or edad > maxima_edad:
            maxima_edad = edad
            bandera = True


for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]

    if genero == 'Masculino' and edad == maxima_edad:
        lista_maxima_edad.append(f'Nombre: {nombre}|Tecnologia: {tecnologia}')
        #print(f"\t{nombre:15}{tecnologia}")


print(f"Cantidad de empleados que cumplen el crtiterio: {contador}")
porcentaje = (contador_ia * 100) / len(lista_tecnologias)
print(f"El porcentaje de empleados es {porcentaje:0.2f}%")
print(f'Maxima edad :{maxima_edad}')
for coincidencia in lista_maxima_edad:
    print(coincidencia)