lista=[1,2,-3,4,5,-1,-7,8,-45]
negativos=[]
positivos=[]

print ("lista original",lista)

for i in lista:
    if i<0:
        negativos.append(i)
    else:
        positivos.append(i)
print("Lista  negativos: ", negativos," Lista positivos: ", positivos)
