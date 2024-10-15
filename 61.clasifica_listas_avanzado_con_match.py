lista=[]
while True:
    entrada = input("Ingrese un número, escribe fin para terminar: ")
    if entrada.lower() == "fin":
        break
    lista.append(int(entrada))
print("Los números introducidos son: ", lista)

positivos = False
negativos = False
for i in lista:
    if i > 0:
        positivos=True
    elif i < 0:
        negativos=True
match (lista, positivos, negativos):
    case ([],_,_):
        print("Lista vacia")
    case (_,True,False):
        print("Contiene solo números positos")
    case (_,False,True):
        print("contiene solo números negativos")
    case(_,True,True):
        print("contiene una mezcla de números positivos y negativos.")
    case _:
        print("contiene otros elementos")


    

        
