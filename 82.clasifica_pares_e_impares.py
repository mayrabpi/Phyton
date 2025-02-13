#Pide al usuario que introduzca una lista de números. Luego, clasifica esos números en un diccionario con dos claves: 
# "pares" y "impares", y almacena en cada clave los números correspondientes

entrada = input("Introduce una lista de números separados por espacios:")
lista_numeros = entrada.split()

numeros=[]
for i in lista_numeros:
    numeros.append(int(i))

clasificacion={"pares":[], "impares":[]}

for i in numeros:
    if i %2==0:
        clasificacion["pares"].append(i)
    else:
        clasificacion["impares"].append(i)

print(f"Pares {clasificacion['pares']}")
print(f"Impares {clasificacion['impares']}")


