#Crea un diccionario que actúe como inventario de una tienda, con productos como claves y su 
# cantidad en stock como valores. Permite al usuario agregar o quitar productos,
#  y modificar las cantidades. Usa bucles y condicionales para manejar las acciones del usuario

inventario = {"camisetas": 10, 
              "pantalones": 5,
               "zapatos": 3, 
               "gorras": 7, 
               "calcetines": 12}


def agregar_producto(producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    return inventario

def eliminar_producto(producto):
    if producto in inventario:
        del inventario[producto]
        return inventario
    
def modificar_cantidad(producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
    else:
        print("El producto no existe en el inventario")
    return inventario
    

def menu():
  while(True):
    print("1. Agregar producto")
    print("2. Quitar producto")
    print("3. Modificar cantidad")
    print("4. Mostrar inventario")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))
    
    match opcion:
        case 1:
            producto= input("Introduce el producto:")
            cantidad= input("Introduce la cantidad:")
            agregar_producto(producto,cantidad)
            print("producto agregado correctamente")
        case 2:
            producto = input("Introduce el producto a eliminar:")
            eliminar_producto(producto)
            print("Producto eliminado correctamente")
        case 3:
            producto = input("Introduce el producto a modificar: ")
            cantidad = input ("Introduce la nueva cantidad:")
            modificar_cantidad(producto, cantidad)
            print("Producto modificado correctamente")
        case 4:
            print(inventario)
        case 5: 
            print("saliendo del programa....")
            break
        case _:
            print("Opción no válida")
            
menu()
