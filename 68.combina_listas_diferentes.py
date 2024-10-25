lista1=[1,2,3,4,5,6,8,10,20,30,50]
lista2=[7,8,9,10,11,12]
max_logitud= max(len(lista1),len(lista2))

lista1_extendida=[]
for i in range(max_logitud):
        if i<len(lista1):
         lista1_extendida.append(lista1[i])
        else:
         lista1_extendida.append(None)


lista2_extendida=[]
for i in range(max_logitud):
        if i<len(lista2):
            lista2_extendida.append(lista2[i])
        else:
         lista2_extendida.append(None)

resultado=[]
for i in range(max_logitud):
    resultado.append((lista1_extendida[i],lista2_extendida[i]))
    
print(resultado)