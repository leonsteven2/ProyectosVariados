# Funciones que tienen un nombre especial reservado
# Inician con __ y terminan con __
# Nos permiten crear funciones especiales que con métodos comunes no podríamos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # str retorna una representación del objeto en una cadena de texto
    def __str__(self):
        return f'Persona(Nombre="{self.nombre}", Edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre + other.nombre, nuevo_valor)

pepe = Persona("Pepe", 21)

# Función __str__ sirve cuando imprimimos el objeto
print(pepe)

# Función __repr__
representacion_del_objeto = repr(pepe)
reconstruyo_objeto = eval(representacion_del_objeto)
print(representacion_del_objeto)
print(reconstruyo_objeto.nombre)
print(reconstruyo_objeto.edad)

# Probamos la función __add__
juan = Persona("Juan", 2)
pedro = Persona("Pedro", 3)
juan_pedro = juan + pedro
print(juan_pedro)

maria = Persona("Maria", 5)
juan_pedro_maria = juan_pedro + maria
print(juan_pedro_maria)