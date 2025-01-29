import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo con Grid")

# Crear widgets y organizarlos con grid
etiqueta1 = tk.Label(ventana, text="Fila 0, Columna 0")
etiqueta1.grid(row=0, column=0, padx=10, pady=10)

etiqueta2 = tk.Label(ventana, text="Fila 0, Columna 1")
etiqueta2.grid(row=0, column=1, padx=10, pady=10)

etiqueta3 = tk.Label(ventana, text="Fila 1, Columna 0")
etiqueta3.grid(row=1, column=0, padx=10, pady=10)

etiqueta4 = tk.Label(ventana, text="Fila 1, Columna 1")
etiqueta4.grid(row=1, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()