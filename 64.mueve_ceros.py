numeros =[0,1,0,3,12,0,5]
lista=[]
listaCeros=[]

for i in numeros:
    if i==0:
        lista.append(i)
    else:
        listaCeros.append(i)
resultado=listaCeros + lista
print(resultado)
