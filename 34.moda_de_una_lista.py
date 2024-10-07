#La moda es el valor más repetido de una lista
# Lista de ejemplo
lista = [1, 2, 3, 3, 4, 5, 3, 2]

# Inicializamos variables para la moda y la mayor frecuencia
moda = None
mayor_frecuencia = 0

# Recorremos la lista para contar la frecuencia de cada número
for i in range(len(lista)):
    contador = 0
    # Contar cuántas veces aparece lista[i] en la lista
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            contador += 1
    # Si encontramos un número con mayor frecuencia, actualizamos la moda
    if contador > mayor_frecuencia:
        mayor_frecuencia = contador
        moda = lista[i]

# Imprimimos el valor de la moda
print("La moda es:", moda)
        






