import tkinter as tk

inventario = {}

def agregar_producto():
    producto = entrada_producto.get()
    cantidad = entrada_cantidad.get()
    precio = entrada_precio.get()
    inventario[producto] = {'cantidad': cantidad, 'precio': precio}
    resultado.set(f"Producto {producto} agregado.")

def buscar_producto():
    producto = entrada_producto.get()
    info = inventario.get(producto, "No encontrado")
    if info != "No encontrado":
        resultado.set(f"{producto} - Cantidad: {info['cantidad']}, Precio: {info['precio']}")
    else:
        resultado.set("Producto no encontrado")

def mostrar_invebtario():
    if inventario:
        inventariostr= "Inventario:\n"
        for producto, info in inventario.items():
            inventariostr+=f"{producto}-Cantidad: {info['cantidad']}- precio:{info['precio']}"
        resultado.set(inventariostr)
    else:
        resultado.set("El inventario esta vacio")
  

ventana = tk.Tk()
ventana.title("Inventario de Productos")
ventana.geometry("400x300")

tk.Label(ventana, text="Producto:").pack(pady=5)
entrada_producto = tk.Entry(ventana, width=30)
entrada_producto.pack(pady=5)

tk.Label(ventana, text="Cantidad:").pack(pady=5)
entrada_cantidad = tk.Entry(ventana, width=30)
entrada_cantidad.pack(pady=5)

tk.Label(ventana, text="Precio:").pack(pady=5)
entrada_precio = tk.Entry(ventana, width=30)
entrada_precio.pack(pady=5)

tk.Button(ventana, text="Agregar", command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="Buscar", command=mostrar_invebtario).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()