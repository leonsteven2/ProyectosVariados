# ISP - Principio de Segregación de la Interfaz
# Ningún cliente debe ser forzado a depender de interfaces que no utilice
from abc import ABC, abstractmethod


# En el siguiente ejemplo:
# La clase robot se ve obligada a crear los métodos comer y dormir aunque sabemos
# que los robots no comen ni duermen

# class Trabajador(ABC):
#
#     @abstractmethod
#     def comer(self):
#         pass
#
#     @abstractmethod
#     def trabajar(self):
#         pass
#
#     @abstractmethod
#     def dormir(self):
#         pass
#
#
# class Humano(Trabajador):
#     def comer(self):
#         print("El humano come")
#
#     def trabajar(self):
#         print("El humano trabaja")
#
#     def dormir(self):
#         print("El humano duerme")
#
#
# class Robot(Trabajador):
#     def trabajar(self):
#         print("El humano trabaja")
#
# robot = Robot()

# Lo correcto sería:

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):

    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):

    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano come")

    def trabajar(self):
        print("El humano trabaja")

    def dormir(self):
        print("El humano duerme")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot trabaja")


robot = Robot()
robot.trabajar()

humano = Humano()
humano.trabajar()
