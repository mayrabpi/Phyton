import tkinter as tk
from tkinter import messagebox

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera interfaz gráfica")

#Función que se ejecuta al hacer clic en el botón
def saludar():
    messagebox.showinfo("Saludo", "¡Hola mundo!")

#Crear un botón
boton = tk.Button(ventana, text="Saludar", command = saludar)
boton.pack(pady = 40)#espacio al rededor 

#Iniciar el bucle principal de la ventana
ventana.mainloop()