# El polimorfismo hace referencia a enviar mensajes a los objetos para que estos
# interactúen o respondan de manera diferente dependiendo de sus atributos o características
# Poli: Muchas
# Morfi: Formas

class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

# Enviamos el mismo mensaje y obtenemos diferentes respuestas dependiendo del objeto
hacer_sonido(gato)
hacer_sonido(perro)
