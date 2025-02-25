import tkinter as tk 

def tabla_multiplicar():
    try:
       numero = int(entrada_numero.get())
       texto_tabla=" "
       for i in range(1,11):
           texto_tabla += f"\n{numero}x{i}={numero*i}"
           resultado.config(text=texto_tabla)
    except ValueError:
        resultado.config(text="¡Ingresa un número válido!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Dia de semana")

# Crear cuadro de entrada para Celsius
entrada_numero = tk.Entry(ventana)
entrada_numero.grid(row=0, column=0, padx=10, pady=10)

# Crear botón para convertir
boton = tk.Button(ventana, text=" Tabla de multiplicar", command=tabla_multiplicar)
boton.grid(row=1, column=0, pady=10)

# Crear etiqueta para mostrar el resultado
resultado= tk.Label(ventana, text="")
resultado.grid(row=2, column=0, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
