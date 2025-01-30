import tkinter as tk

def dia_semana():
    try:
        dia = int(entrada_dia.get())
        if dia == 1:
            resultado.config(text="Lunes")
        elif dia == 2:
            resultado.config(text="Martes")
        elif dia == 3:
            resultado.config(text="Miércoles")
        elif dia == 4:
            resultado.config(text="Jueves")
        elif dia == 5:
            resultado.config(text="Viernes")
        elif dia == 6:
            resultado.config(text="Sábado")
        elif dia == 7:
            resultado.config(text="Domingo")
        else:
            resultado.config(text="¡Ingresa un número entre 1 y 7!")
    except ValueError:
        resultado.config(text="¡Ingresa un número válido!")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Dia de semana")

# Crear cuadro de entrada para Celsius
entrada_dia = tk.Entry(ventana)
entrada_dia.grid(row=0, column=0, padx=10, pady=10)

# Crear botón para convertir
boton = tk.Button(ventana, text=" Dia semana", command=dia_semana)
boton.grid(row=1, column=0, pady=10)

# Crear etiqueta para mostrar el resultado
resultado= tk.Label(ventana, text="")
resultado.grid(row=2, column=0, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()