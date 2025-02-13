import tkinter as tk
ventana = tk.Tk()
def mostrar_seleccion():
    if check_var.get() == 1:
        print("Casilla marcada")
    else:
        print("Casilla desmarcada")

check_var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Acepto los términos", variable=check_var, command=mostrar_seleccion)
check.pack(pady=10)

ventana.mainloop()