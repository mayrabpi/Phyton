lista=[5,4,3,9,8,5,6,3,2,1]
print(lista)
for i in range(len(lista)):
    for j in range(len(lista)-i-1):
        if lista[j]>lista[j+1]:
            aux=lista[j+1]
            lista[j+1]=lista[j]
            lista[j]= aux

print ("Lista ordenada: ", lista)

