lista=[1,2,3,4,5,6]
lista1=[]

i=len(lista)

while(i>=1):
    lista1.append(lista[i-1])
    i-=1
print(lista1)
