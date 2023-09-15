# El encapsulamiento consiste en proteger los elementos de una clase
# Oculta cierta complejidad interna que existe dentro de la clase y protege los atributos cuando se ponen privada
# Mejora la legibilidad del código
# La forma de decirle a python que un atributo es privado es añadiendo un "_" después de self.

class MiClase:
    def __init__(self):
        self._atributo_privado = "Atributo privado"  # Atributo privado
        self.__atributo_privado = "Atributo muy privado"  # Atributo muy privado

    def __metodo_muy_privado(self):
        print("Este es un método muy privado")

    def get_atributo_privado(self):
        return self._atributo_privado

    def get_atributo_muy_privado(self):
        return self.__atributo_privado

    def set_atributo_privado(self, value):
        self._atributo_privado = value

    def set_atributo_muy_privado(self, value):
        self.__atributo_privado = value

objeto = MiClase()
print(objeto._atributo_privado)  # El desarrollador sabe que es privado, pero puede acceder a este atributo

# Para establecer un atributo muy muy privado con "__"
# print(objeto.__atributo_privado)  # No permite acceder porque salta error
# objeto.__metodo_muy_privado

# Para acceder a los datos encapsulados se usan getters (accede al atributo) y setters (modifica)
# SETTERS
objeto.set_atributo_privado("Atributo privado modificado")
objeto.set_atributo_muy_privado("Atributo muy privado modificado")
# GETTERS
atributo_privado = objeto.get_atributo_privado()
print(atributo_privado)
atributo_muy_privado = objeto.get_atributo_muy_privado()
print(atributo_muy_privado)
