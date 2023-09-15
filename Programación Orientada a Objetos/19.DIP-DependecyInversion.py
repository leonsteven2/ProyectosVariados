# DIP - Principio de Inversión de Dependencia
# Establece dos cosas:
# 1. Los módulos de alto nivel no tienen que depender de los de bajo nivel, los dos deben depender de las abstracciones
# 2. Las abstracciones no deben depender de los detalles, los detalles dependen de las abstracciones


# En el siguiente ejemplo, el corrector ortografico depende de diccionario
# para realizar su corrección
# Si el día de mañana queremos cambiar la manera de corregir, en vez de diccionario
# queremos que sea por internet u otro método
# Al cambiar diccionario debemos cambiar toda la clase corrector ortografico
# Básicamente la clase Corrector Ortografico es mucho más importante que la clase Diccionario
# Como en el caso de la clase Auto, Auto no puede depender de tanque
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         # Aquí va la lógica para verificar palabras
#         pass
#
#
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
#
#     def corregir_texto(self, texto):
#         # Usamos el objeto diccionario para corregir el texto
#         pass


# En el siguiente ejemplo, la clase corrector ortográfico ya no depende
# de diccionario, sino que depende de la implementación de VerificadorOrtográfico
# que a su vez puede ser diccionario o servicio web
from abc import ABC, abstractmethod


class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si esta en el diccionario
        pass


class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras usando servicio web
        pass


class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Usamos el verificador para corregir texto
        pass

corrector_por_diccionario = CorrectorOrtografico(Diccionario)
corrector_por_servicio_web = CorrectorOrtografico(ServicioOnline)





