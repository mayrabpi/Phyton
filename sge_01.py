numero1=int(input("Dime el primer número:"))
numero2=int(input("Dime el segundo números:"))
cantidadGenerar = int(input("Cantidad a generar"))
aleatorio=[]
aleatorio1=[]
for i in range(numero1,numero2):
    aleatorio.append(i) 
    
    for j in range(len(aleatorio),cantidadGenerar+1,numero2):
        aleatorio1.append(j)
        aleatorio1.reverse()
    
print(aleatorio1)




      
            

              



