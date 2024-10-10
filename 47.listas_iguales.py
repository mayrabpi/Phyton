#Compara dos listas y determina si contienen los mismos elementos, sin tener en cuenta el orden.

lista=[1,2,3,4,5]
lista1=[2,3,4,1]

lista.sort()
lista1.sort()
if lista == lista1:
    print("Tienen los mismos elementos")
else:
    print("no son iguales")