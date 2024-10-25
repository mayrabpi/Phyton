#sin metodos, ordenamos una lista con el metodo de la burbuja
lista=[4,5,7,10,8,9,6,3,11,20,25]

print(lista)
for i in range(len(lista)):
    for j in range(len(lista)-i-1):
        if lista[j]>lista[j+1]:
            aux=lista[j+1]
            lista[j+1]=lista[j]
            lista[j]= aux
print(lista)
print(f"El segundo mayor es {lista[-2]}")

