# ¿Nuestro código va a durar o se va a extender,
# Es un programa que en el futuro va a crecer más?
# 1. Mantenibilidad: Software fácil de mantener y modificar en el tiempo
# 2. Reusabilidad: Todos los componentes deben ser reutilizables
# 3. Legibilidad: El código debe ser fácil de entender
# 4. Extensibilidad: Debe permitir la capacidad de extenderse sin afectar el código

# Principios SOLID
# 1. S: SRP - SINGLE RESPONSIBILITY PRINCIPLE
# Cada clase debe tener una única responsabilidad o tarea
# Si notamos que una clase debe hacer una funcionalidad diferente
# es mejor esperar la clase en dos clases
# El objetivo es evitar clases sobrecargadas y que cada clase trabaje independiente de otras

# En el siguiente ejemplo se muestra que la clase Auto() tiene dos responsabilidades
# Mover el auto y cargar el combustible
# class Auto():
#     def __init__(self):
#         self.posicion = 0
#         self.combustible = 100
#
#     def mover(self, distancia):
#         if self.combustible >= distancia/2:
#             self.posicion += distancia
#             self.combustible -= distancia/2
#         else:
#             print("No hay suficiente combustible")
#
#     def agregar_combustible(self, cantidad):
#         self.combustible += cantidad
#
#     def obtener_combustible(self):
#         return self.combustible

# Lo correcto es:
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"Has movido el auto {self.posicion} m")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return f'La posición actual del auto es: {self.posicion} m'


tanque = TanqueDeCombustible()
mi_auto = Auto(tanque)

print(mi_auto.obtener_posicion())
mi_auto.mover(10)
print(mi_auto.obtener_posicion())
mi_auto.mover(20)
print(mi_auto.obtener_posicion())
mi_auto.mover(400)
print(mi_auto.obtener_posicion())
