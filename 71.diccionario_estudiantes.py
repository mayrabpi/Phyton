diccionario={"pepe":"P","ana":"A","juan":"P","maria":"P"}

nombre=input("ingrese el nombre:")

print(diccionario.get(nombre.lower(),"no existe"))