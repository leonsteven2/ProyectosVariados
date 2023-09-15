class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_nombre_y_edad(self):
        print(f'El nombre es: {self.nombre} y su edad es {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super(Estudiante, self).__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        print(f'El grado es: {self.grado}')

nombre = "Steven"
edad = 23
grado = 8

estudiante = Estudiante(nombre, edad, grado)
estudiante.imprimir_nombre_y_edad()
estudiante.imprimir_grado()
