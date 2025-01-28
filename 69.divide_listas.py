def dividir_lista(lista, n):
    longitud = len(lista)
    tamano_base = longitud // n
    extra = longitud % n

    sublistas = []
    inicio = 0

    for i in range(n):
        # Determinar el tamaño de la sublista actual
        if i < extra:
            tamano_sublista = tamano_base + 1
        else:
            tamano_sublista = tamano_base
        
        # Obtener la sublista desde 'inicio' hasta 'inicio + tamano_sublista'
        sublista = lista[inicio:inicio + tamano_sublista]
        sublistas.append(sublista)
        # Actualizar el índice 'inicio' para la siguiente sublista
        inicio += tamano_sublista

    return sublistas

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7]
n = 2
resultado = dividir_lista(lista, n)
print(resultado)  # [[1, 2, 3, 4], [5, 6, 7]]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 3
resultado = dividir_lista(lista, n)
print(resultado)  # [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20]]
