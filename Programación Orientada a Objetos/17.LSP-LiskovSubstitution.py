# Las clases derivadas deben ser sustituibles por sus clases base
# Si la clase B es una subclase de A
# La clase A debería poder utilizarse en todos los lugares en donde B pueda utilizarse

# En el siguiente ejemplo, cuando instanciamos un objeto pinguino
# y lo queremos hacer volar por medio de la función
# este no vuela porque en la lógica real y de programación esto no es posible
# Sin embargo, pinguino si pertenece a la clase Ave donde volar es posible
# class Ave:
#     def volar(self):
#         return "Estoy Volando"
#
#
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
#
#
# def hacer_volar(ave=Ave):
#     return ave.volar()
#
#
# print(hacer_volar(Pinguino()))

# Para resolver este problema se utiliza este principio SRP
# En la clase Ave se establecen todas las características en común que tienen las aves
class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"


class AveNoVoladora(Ave):
    pass
