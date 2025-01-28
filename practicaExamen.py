
"""import random
def crar_tablero(filas,columnas):
    simbolos=['a','b','c','d','f','g','h']
    simbolos = simbolos[:(filas*columnas)//2]*2
    random.shuffle(simbolos)
    tablero=[]
    posicion=0

    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(simbolos[posicion])
            posicion+=1
        tablero.append(fila)
    return tablero


def tablaro_oculto(filas,columnas):
    oculto=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append('*')
        oculto.append(fila)
    return oculto


def mostrar(tablero):
    for i in tablero:
        print(' '.join(i))


while True:
    filas = int(input('introduce num filas: '))
    columnas= int(input('introduce num columnas: '))
    if 2<=filas <=6 and 2<=columnas<=5 and (filas*columnas)%2 ==0:
        break
    else :
     print('introduce dimenciones validas')



tablero=crar_tablero(filas,columnas)
oculto= tablaro_oculto(filas,columnas)
mostrar(oculto)
mostrar(tablero) """
def crear_tablero():
    # Pedir al usuario el número de filas y columnas
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    # Generar el tablero
    for _ in range(filas):  # Repetir para cada fila
        print("* " * columnas)  # Imprimir una fila con el número de columnas de asteriscos

# Llamar a la función
crear_tablero()

import random

def crear_tablero_emojis():
    # Pedir al usuario el número de filas y columnas
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    
    # Definir una lista de emojis
    emojis = ["🔴", "🟢", "🔵", "🟡", "🟣", "🟠"]
    
    # Generar el tablero con emojis aleatorios
    for _ in range(filas):
        fila = [random.choice(emojis) for _ in range(columnas)]  # Seleccionar un emoji aleatorio por celda
        
        print(" ".join(fila))  # Unir los emojis en una fila con espacios entre ellos

# Llamar a la función
crear_tablero_emojis()

filas=2
colum=2
for _ in range(filas):
    print("*"*colum)


