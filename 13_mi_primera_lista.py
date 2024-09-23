
lista=[]
while True:
    entrada = input("Ingrese un número, escribe fin para terminar: ")
    if entrada.lower() == "fin":
        break
    lista.append(entrada)
print("Los números introducidos son: ", lista)

print("El primer número introducido es: ", lista[0])
print("El último número introducido es: ", lista[-1])