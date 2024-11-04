numero=int(input("ingrese un número entero:"))

a=0
b=1
for i in range( numero):
   
    a,b =b,a+b
    print(a, end=' ')
 
