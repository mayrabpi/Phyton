lista=[1,2,3,4,5,6,7]
print(lista)
numero= int(input("Introduze el número que desea reemplazar:"))
nuevo_numero=int(input("Introduze su reemplazo:"))


for i in range(len(lista)):
    if lista[i]==numero:
        lista[i]=nuevo_numero
print("lista actualizada: ", lista)
    
        