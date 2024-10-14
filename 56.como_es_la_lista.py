lista=[1,2,3]
match lista:
    case []:
        print("Lista vacia")
    case [elemento]:
        print(f"lista con un elemento: {elemento}")
    case _:
        print(f"lista con mas elementos: {len(lista)} elementos tiene la lista")
    
