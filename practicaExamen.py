import random
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
mostrar(tablero)

