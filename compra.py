import tkinter as tk
from tkinter import messagebox

# Diccionario inicial del inventario
inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "gorras": 7, "calcetines": 12}

# Funciones para manejar el inventario
def agregar_producto():
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()
    if producto and cantidad:
        if producto in inventario:
            inventario[producto] += int(cantidad)
        else:
            inventario[producto] = int(cantidad)
        messagebox.showinfo("Éxito", f"Producto '{producto}' agregado/modificado correctamente.")
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Por favor, ingresa un producto y una cantidad.")

def eliminar_producto():
    producto = entry_producto.get()
    if producto in inventario:
        del inventario[producto]
        messagebox.showinfo("Éxito", f"Producto '{producto}' eliminado correctamente.")
        entry_producto.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", f"El producto '{producto}' no existe en el inventario.")

def modificar_cantidad():
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()
    if producto in inventario and cantidad:
        inventario[producto] = int(cantidad)
        messagebox.showinfo("Éxito", f"Cantidad de '{producto}' modificada correctamente.")
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Por favor, ingresa un producto existente y una cantidad.")

def mostrar_inventario():
    inventario_text = "\n".join([f"{k}: {v}" for k, v in inventario.items()])
    messagebox.showinfo("Inventario", inventario_text)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Inventario")

# Creación de los widgets
label_producto = tk.Label(root, text="Producto:")
label_producto.grid(row=0, column=0, padx=10, pady=10)

entry_producto = tk.Entry(root)
entry_producto.grid(row=0, column=1, padx=10, pady=10)

label_cantidad = tk.Label(root, text="Cantidad:")
label_cantidad.grid(row=1, column=0, padx=10, pady=10)

entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=1, column=1, padx=10, pady=10)

button_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
button_agregar.grid(row=2, column=0, padx=10, pady=10)

button_eliminar = tk.Button(root, text="Eliminar Producto", command=eliminar_producto)
button_eliminar.grid(row=2, column=1, padx=10, pady=10)

button_modificar = tk.Button(root, text="Modificar Cantidad", command=modificar_cantidad)
button_modificar.grid(row=3, column=0, padx=10, pady=10)

button_mostrar = tk.Button(root, text="Mostrar Inventario", command=mostrar_inventario)
button_mostrar.grid(row=3, column=1, padx=10, pady=10)

# Iniciar la aplicación
root.mainloop()













