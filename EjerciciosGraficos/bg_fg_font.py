import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Personalización con bg, fg y font")

# Configurar el color de fondo de la ventana
ventana.config(bg="lightblue")

# Crear una etiqueta con colores y fuente personalizados
etiqueta = tk.Label(
    ventana,
    text="¡Hola, Tkinter!",
    bg="navy",          # Color de fondo
    fg="white",         # Color del texto
    font=("Arial", 20)  # Fuente y tamaño
)
etiqueta.pack(pady=20)

# Crear un botón con colores y fuente personalizados
boton = tk.Button(
    ventana,
    text="Haz clic aquí",
    bg="green",         # Color de fondo
    fg="yellow",        # Color del texto
    font=("Helvetica", 14, "bold")  # Fuente, tamaño y negrita
)
boton.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()