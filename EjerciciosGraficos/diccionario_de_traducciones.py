import tkinter as tk

diccionario = {}

def agregar_palabra():
    palabra = entrada_palabra.get()
    traduccion = entrada_traduccion.get()
    diccionario[palabra] = traduccion
    resultado.set(f"Palabra {palabra} agregada.")

def buscar_traduccion():
    palabra = entrada_palabra.get()
    traduccion = diccionario.get(palabra, "No encontrada")
    resultado.set(f"Traducción de {palabra}: {traduccion}")

ventana = tk.Tk()
ventana.title("Diccionario de Traducción")
ventana.geometry("400x300")

tk.Label(ventana, text="Palabra:").pack(pady=5)
entrada_palabra = tk.Entry(ventana, width=30)
entrada_palabra.pack(pady=5)

tk.Label(ventana, text="Traducción:").pack(pady=5)
entrada_traduccion = tk.Entry(ventana, width=30)
entrada_traduccion.pack(pady=5)

tk.Button(ventana, text="Agregar", command=agregar_palabra).pack(pady=5)
tk.Button(ventana, text="Buscar", command=buscar_traduccion).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()