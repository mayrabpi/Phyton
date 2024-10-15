

lista=[]
while True:
    entrada = input("Ingrese un número, escribe fin para terminar: ")
    if entrada.lower() == "fin":
        break
    lista.append(entrada)
print("Los números introducidos son: ", lista)
lista1=[]
while True:
    entrada = input("Ingrese un número, escribe fin para terminar: ")
    if entrada.lower() == "fin":
        break
    lista1.append(entrada)
print("Los números introducidos son: ", lista1)

match lista:
    case _ if(lista==lista1):
        print("Son iguales")
    case _ if(sorted(lista)== sorted(lista1)):
        print("tienen los mismo elementos, pero en distinto orden")
    case _ if(len(lista)!=len(lista1)):
        print("tienen diferentes tamaños")
    case _ if (sorted(lista)!= sorted(lista1)):
        print("no tienen elementos en comun")



