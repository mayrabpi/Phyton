diccionario={"movil":3000,"telefono":500,"computador":1000}

producto=input("ingrese el nombre del producto:")

print(diccionario.get(producto,"no existe"),"€")