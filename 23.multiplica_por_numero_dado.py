numeroDado=int(input("Introduzca un número: "))
lista_original =[1,2,3,4,5]
lista_multiplicada=[]
print(F"Lista original: {lista_original}")
for i in lista_original:
    lista_multiplicada.append(i*numeroDado)
print(F"Lista multiplicada x {numeroDado}: {lista_multiplicada}")

#otra forma 
lista_multiplicada1=[i*numeroDado for i in lista_original]
print(lista_multiplicada1)