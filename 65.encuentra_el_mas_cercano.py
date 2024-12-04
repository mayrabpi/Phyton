
# Lista de números
numeros = [10, 22, 35, 47, 55, 66, 78]

# Número proporcionado por el usuario
numero_objetivo = int(input("Introduce un número: "))

# Encontrar el número más cercano
numero_mas_cercano = numeros[0]
for numero in numeros:
    if (numero - numero_objetivo) ** 2 < (numero_mas_cercano - numero_objetivo) ** 2:
        numero_mas_cercano = numero

print(f"El número más cercano a {numero_objetivo} en la lista es {numero_mas_cercano}.")



