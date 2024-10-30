class Perro():
    especie = "mamifero"
    def __init__(self, nombre, raza):
        print(f"creando perro {nombre} de raza {raza}")

    def ladrar(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

    @classmethod
    def metodeclase (cls):
        return "Método de clase", cls
    

mi_perro = Perro("Toby", "Bulldog")
print(type(mi_perro))
mi_perro.ladrar()
mi_perro.camina(10)