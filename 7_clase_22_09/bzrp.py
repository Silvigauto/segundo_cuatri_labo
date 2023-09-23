from data import *

#"title": 'QUEVEDO' || BZRP Music Sessions #52

def prueba_1():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    parte1 = titulo.split("||")
    artista = parte1[0].strip()
    parte2 = parte1[1].split("#")
    tipo = parte2[0].strip()
    numero = parte2[1].strip()
    print(f"{numero} - {tipo} - {artista}")

def prueba_2(titulo:str):
    parte1 = titulo.split("||")
    artista = parte1[0].strip()
    parte2 = parte1[1].split("#")
    tipo = parte2[0].strip()
    numero = parte2[1].strip()
    print(f"{numero} - {tipo} - {artista}")

#'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
def prueba_3(url:str, lista:list):
    #metodo 4
    indice = url.index("=")
    codigo = url[indice+1:]

    #metodo 3
    #codigo = url.replace('https://youtube.com/watch?v=', '')

    #metodo 2
    # partes = url.split('=')
    # codigo = partes[1]

    #metodo 1
    # codigo = url[28:]
    print(codigo)
    lista.append(codigo)

def formatear_fecha(tema:dict):
    fecha_string = tema['date']
    fecha_split = fecha_string.split(" ")
    fecha = fecha_split[0].split('-')
    dia = fecha[2]
    mes = fecha[1]
    año = fecha[0]
    separador = '/'
    fecha_formato = separador.join([dia, mes,año])
    print(fecha_formato)

lista = []
for tema in lista_bzrp:
    #prueba_3(tema['url'],lista)
    formatear_fecha(tema['date'])


print(len(lista))
# #solo muestra los titulos q cumplen con ese formato
# for tema in lista_bzrp:
#     if tema['title'].find('||') >= 0 and tema['title'].find('#') >= 0:
#         prueba_2(tema['title']) 