cadena= input("introduce una palabra")
vocales= ["a","e","i","o","u"]
contador=0

for i in cadena:
    if i in vocales:
        contador+=1

print(contador)

