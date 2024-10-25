lista=[1,2,3,4,6,7,8,9,10]
numeroDado=int(input("Ingrese un numero: "))

for i in lista:
    if lista[i]==numeroDado:
        print(f"numero {numeroDado} no econtrado, el mas cercano es {i}")


