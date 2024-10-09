numeros=[1,3,4,2,8,9]
numeroDado=int(input("Diga un número: "))
listamax=[]
listamin=[]

for i in range(len(numeros)):
    if numeros[i]>numeroDado:
        listamax.append(numeros[i])
    else:
        if numeros[i]<numeroDado:
            listamin.append(numeros[i])

print(listamax)
print(listamin)

