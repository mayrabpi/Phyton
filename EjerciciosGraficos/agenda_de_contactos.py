import tkinter as tk
contactos={}

def añadir_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    contactos[nombre]= telefono
    resultado.set("Cpntacto añadido correctamente")

def mostrar_contacto():
    todos_contactos = "\n".join([f"{nombre}:{telefono}" for nombre, telefono in contactos.items()])
    resultado.set(f"Contactos:\n{todos_contactos}")




ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entrada_nombre= tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)


tk.Label(ventana, text="Teléfono:").pack(pady=5)
entrada_telefono = tk.Entry(ventana, width=30)
entrada_telefono.pack(pady=5)

tk.Button(ventana, text="Añadir contacto" , command=añadir_contacto).pack(pady=5)
tk.Button(ventana, text="Mostrar contactos", command=mostrar_contacto).pack(pady=5)
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)


ventana.mainloop()