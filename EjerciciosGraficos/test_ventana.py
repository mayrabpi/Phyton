import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al hacer clic en el botón "Saludar"
def saludar():
    nombre = entrada_nombre.get()  # Obtener el texto del cuadro de entrada
    if nombre:
        messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")
    else:
        messagebox.showwarning("Error", "Por favor, ingresa tu nombre.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludador")
ventana.geometry("300x200")  # Tamaño de la ventana (ancho x alto)

# Crear un Frame para organizar los widgets
marco = tk.Frame(ventana)
marco.pack(pady=20)

# Crear una etiqueta (Label)
etiqueta = tk.Label(marco, text="Ingresa tu nombre:")
etiqueta.grid(row=0, column=0, padx=10, pady=10)

# Crear un cuadro de entrada (Entry)
entrada_nombre = tk.Entry(marco)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

# Crear un botón (Button)
boton_saludar = tk.Button(marco, text="Saludar", command=saludar)
boton_saludar.grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()