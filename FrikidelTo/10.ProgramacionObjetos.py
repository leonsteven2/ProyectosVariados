# Clase para crear objetos Soldado
class Soldado:
    # Atributos de clase(valores por defecto para los nuevos objetos)
    vuela = False
    velocidad = 3

    # constructor
    def __init__(self, nivel):
        # Atributos de instancia (se definen al crear el objeto)
        self.nivel = nivel
        self.vida = nivel * 1000
        self.fuerza = nivel * 100

    # Método que habilita al objeto la capacidad de volar
    def coger_alas(self):
        self.vuela = True

    # Método que resta daño a la vida del objeto
    def recibe_dano(self, dano):
        self.vida -= dano

# Instanciamos la tropa 1
tropa1 = Soldado(10)
print(f'Nivel: {tropa1.nivel} ; Vida: {tropa1.vida} ; Fuerza: {tropa1.fuerza}')
print(tropa1.vuela)
tropa1.coger_alas()
print(tropa1.vuela)

# Instanciamos la tropa 2
tropa2 = Soldado(20)
print(f'Nivel: {tropa2.nivel} ; Vida: {tropa2.vida} ; Fuerza: {tropa2.fuerza}')
tropa2.recibe_dano(500)
print(tropa2.vida)


