#Verifica si todos los números de una lista son positivos
lista=[1,2,3,4,5,-2]
for i in lista:
    if(i<0):
        negativos=True
    else:
        negativos= False

if negativos==True:
    print("Hay numero negativos")
else:
    print("Lista de números positivos")
