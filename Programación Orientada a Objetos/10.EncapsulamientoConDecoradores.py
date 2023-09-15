class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


objeto = Persona("Lucas", 23)
# El getter me permite acceder a la variable muy privada
print(objeto.nombre)
# El setter permite modificarlo
objeto.nombre = "Pepe"
print(objeto.nombre)

# Deleter permite borrar esa propiedad
del objeto.nombre
try:
    print(objeto.nombre)
except AttributeError:
    print("El atributo no existe")

