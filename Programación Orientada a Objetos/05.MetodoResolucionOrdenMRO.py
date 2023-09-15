# El MRO es un método que hace referencia al orden en que Python
# Busca métodos y atributos en las clases

class A:
    def hablar(self):
        print("Hola desde la clase A")


class B(A):
    def hablar(self):
        print("Hola desde la clase B")


class C(A):
    def hablar(self):
        print("Hola desde la clase C")


class D(B, C):
    # def hablar(self):
    #     print("Hola desde la clase D")
    pass


d = D()
d.hablar()  # La jerarquía es la siguiente: D -> B -> C -> A

# Lo podemos comprobar con la siguiente línea de código
print(D.mro())

# Podemos ejecutar la función directamente
B.hablar(d)
