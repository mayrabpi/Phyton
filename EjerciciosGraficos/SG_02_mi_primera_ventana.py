import tkinter as tk

def numeroPar():
    try:
        numero = int(entrada_numero.get())
        if numero % 2 == 0:
            resultado.config(text=f"El número {numero} es par")
        else:
            resultado.config(text=f"El número {numero} es impar")
    except ValueError:
        resultado.config(text="¡Ingresa un número válido!")

ventana = tk.Tk()
ventana.title("Verificador de Número Par o Impar")


entrada_numero = tk.Entry(ventana)
entrada_numero.grid(row=0, column=0, padx=10, pady=10)


boton_verificar = tk.Button(ventana, text="Verificar", command=numeroPar)
boton_verificar.grid(row=0, column=1, padx=10, pady=10)


resultado = tk.Label(ventana, text="")
resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()













