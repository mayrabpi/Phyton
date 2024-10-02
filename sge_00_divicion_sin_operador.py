dividendo=int(input("Introduce divisor"))
divisor=int(input("Introduce dividendo"))
cociente=0

i=dividendo

while(i>=divisor):
    i-=divisor
    cociente+=1
print("El cocienete de ", dividendo, "entre ", divisor, "es: ", cociente, "El resto es: " ,i)  

