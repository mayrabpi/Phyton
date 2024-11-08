'''
numero=int(input("ingrese un número entero:"))

a=0
b=1
for i in range( numero+1):
   
    a,b =b,a+b
    print(a, end=' ')'''

n=5
for i in range(1,n+1):
    j=1
    while j<=n-i:
        print(" ", end=" ")
        j+=1
    j=1
    while j<= 2*i-1:
        print("*", end=" ")
        j+=1

    print() 

