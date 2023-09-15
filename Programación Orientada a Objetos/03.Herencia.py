# La herencia se basa en heredar atributos o propiedades a otras clases
# Por ejemplo tenemos la clase padre (Persona) y la clase hija (estudiante, Bombero, etc.)
# Un estudiante o bombero tienen las propiedades de persona, pero tienen diferentes métodos o atributos adicionales
# Para que una clase herede propiedades de otra se debe declarar como:
# class ClaseHija(ClasePadre):

class Persona:
    def __init__(self, nombre, edad, personalidad):
        self.nombre = nombre
        self.edad = edad
        self.personalidad = personalidad

    def hablar(self):
        print("Estas hablando")


class Empleado(Persona):
    def __init__(self, nombre, edad, personalidad, trabajo, salario):
        super().__init__(nombre, edad, personalidad)  # Se especifica que atributos va a heredar de la clase padre
        self.trabajo = trabajo
        self.salario = salario


roberto = Empleado("Roberto", 43, "Argentino", "Bombero", 1000)

print(roberto.trabajo)
roberto.hablar()

