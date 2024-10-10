#Verifica si una lista de elementos se lee igual de izquierda a derecha que de derecha a izquierda.
palabra=input("una palabra: ").lower()
nueva = palabra
nueva=list(nueva)
nueva.reverse()
if(list(palabra)==nueva):
    print("Es palindroma")
else:
    print("No es palindroma")




