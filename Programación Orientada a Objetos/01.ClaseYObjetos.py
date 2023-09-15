# Por convención, la primera letra va con mayúsculas y Pascal Case: Palabra1Palabra2
class NombreClase():
    propiedad1 = "Valor 1"
    propiedad2 = "Valor 2"
    propiedad3 = "Valor 3"


class Celular:
    # Constructor: Se ejecuta primero al instanciar esta clase
    # El Constructor construye los objetos (celulares) con las propiedades marca, modelo, camara
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def enviar_mensajes(self):
        pass

    def llamar(self):
        print(f"Estas llamando desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste desde un {self.modelo}")


celular1 = Celular("Samsung", "S23", "48 MP")
celular2 = Celular("Apple", "Iphone 13", "96 MP")
print(celular2.camara)
celular1.llamar()
celular2.cortar()
