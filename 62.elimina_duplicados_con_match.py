lista = [[1, 2, 3],[4, 2, 3], [6, 5, 4]]
print(sorted(lista))

match lista:
    case lista if(len(lista) == 0):
        print("La lista está vacía ") 
    case lista if(sorted(lista)[0] == sorted(lista)[1]):
        lista.remove(lista[0])
        print(f"Hay sublistas duplicadas, eliminando una... La nueva lista es {lista}")
    case _:
        print(f"En la lista no hay duplicados, la lista es {lista}")