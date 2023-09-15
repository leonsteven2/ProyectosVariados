# La herencia multiple es una clase que hereda de dos o más clases padres
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.personalidad = nacionalidad

    def hablar(self):
        print("Estas hablando")


class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa

    def mostrar_habilidad(self):
        print("Esto es sin usar super().mostrar_habilidad")

    def presentarse(self):
        self.mostrar_habilidad()     # Llamamos a la función de esta clase si estuviera creada, caso contrario, accedemos a las funciones del padre
        super().mostrar_habilidad()  # con super() llamamos a la función de la clase padre de manera directa

roberto = EmpleadoArtista("Roberto", 43, "Argentino", "Cantar", 1000 , "Facebook")
roberto.presentarse()

# Como saber si una clase hereda propiedades de otra clase
print(issubclass(EmpleadoArtista,Artista))

# Como saber si un objeto es instancia de una clase
print(isinstance(roberto, Persona))
print(isinstance(roberto, Artista))
print(isinstance(roberto, EmpleadoArtista))
