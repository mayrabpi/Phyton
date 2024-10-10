lista=[1,2,3,4,5,6,7,8,9,10,11,15]
par =0
impar=0

for i in lista:
    if i%2==0:
        par+=1
    else:
        impar+=1

print(f"en la lista de {lista} hay {par} pares y {impar} impares")
