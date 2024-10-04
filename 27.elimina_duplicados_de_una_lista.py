lista=[2,1,5,6,3,1,9,9,10,11,1,25]
listaRepetidos=[]
print(lista)
#ordenamos con el método de la burbuja, 
for i in range(len(lista)):
    for j in range(len(lista)-i-1):
        if lista[j]>lista[j+1]:
            aux = lista[j+1]
            lista[j+1] = lista[j]
            lista[j]=aux
        
i=0
while i< len(lista)-1:
        if lista[i]==lista[i+1] :
           
            listaRepetidos.append(lista[i])
            lista.pop(i)
        else:
             i+=1

print(lista)
print(listaRepetidos)




