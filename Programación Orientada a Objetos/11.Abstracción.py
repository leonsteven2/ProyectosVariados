# La abstracción es manejar la complejidad, ocultando todas las funcionalidades
# innecesarias al usuario y dándole las funcionalidades relevantes
# Crear una interfaz simple que oculte la interfaz compleja

class Auto:
    def __init__(self):
        self.__estado = "Apagado"

    def encender(self):
        self.__estado = "Encendido"
        print("El auto está encendido")

    def conducir(self):
        if self.__estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()

# Básicamente, cuando el usuario accede a la función conducir() de mi_auto
# Él no sabe la lógica que hay detrás para encender y conducir el auto


