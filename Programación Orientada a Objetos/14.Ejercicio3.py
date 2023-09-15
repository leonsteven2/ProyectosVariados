# Fusionar personajes de dragon ball
class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    def __add__(self, other):
        nuevo_nombre = self.nombre + "-" + other.nombre
        nueva_fuerza = round(((self.fuerza + other.fuerza)/2)**1.1)
        nueva_velocidad = round(((self.velocidad + other.velocidad)/2)**1.1)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 100, 100)
print(goku)
vegetta = Personaje("Vegetta", 80, 90)
print(vegetta)

vegitta = goku + vegetta
print(vegitta)

