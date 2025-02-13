from tkinter import*

def suma():
    try:
        num1= int(num1_entry.get())
        num2 = int(num2_entry.get())
        resultado.config(text= f"Resultado: {num1+num2}")
    except ValueError:
        resultado.config(text=f"Ingrese números validos ")

def resta():
    try:
        num1 = int(num1_entry.get())
        num2=int(num2_entry.get())
        resultado.config(text=f"Resultado: {num1-num2}")
    except ValueError:
        resultado.config(text=f"Ingrese números validos ")
    


#configuracion de la ventana
ventana =Tk()
#ventana.geometry("400x300")
#ventanas
num1_entry= Entry(ventana)
num1_entry.grid(row=0,column=0,padx=10,pady=10)
num2_entry= Entry(ventana)
num2_entry.grid(row=0,column=2,padx=10,pady=10)
#boton

boton= Button(ventana,text="Suma", command=suma)
boton.grid(row=1,column=1)
boton2 = Button(ventana, text="restar", command=resta)
boton2.grid(row=1, column=0)

#frame sultado
resultado_frame = Frame(ventana,borderwidth=2, relief="sunken" )
resultado_frame.grid(row=2, column=1 , padx=10, pady=10, sticky="ew")
# crear etiqueta para frame

resultado = Label(resultado_frame, text="resultado")
resultado.pack(padx=10,pady=10)















ventana.mainloop()
