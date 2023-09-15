# Las clases abstractas son clases que no podemos instanciar
# Pero que sirven como base o plantilla para crear otras clases
from abc import ABC, abstractclassmethod


# Creamos la plantilla Persona
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")


# Creamos las clases que heredan de la clase abstracta
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Soy estudiante y {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Soy trabajador y {self.actividad}")


Pepe = Estudiante("Pepe", 21, "Masculino", "Programador")
Pepe.presentarse()
Pepe.hacer_actividad()

Jose = Trabajador("Jose", 23, "Masculino", "Bombero")
Jose.presentarse()
Jose.hacer_actividad()
