#Crea una lista de números y cuenta cuántas veces aparece cada número en la lista,
# sin utilizar métodos de python.

lista = [1, 2, 3, 3]

for i in range(len(lista)):
    contador = 0
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            contador += 1
    if lista.index(lista[i]) == i:
        print(lista[i]," . ", contador)
    