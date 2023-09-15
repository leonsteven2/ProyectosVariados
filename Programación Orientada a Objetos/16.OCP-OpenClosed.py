# OCP - OPEN/CLOSED PRINCIPLE
# Las entidades de software (clases, modulos, funciones) tienen que estar abiertas
# para la extensión pero cerradas para la modificación

# Open for extension, closed to modify
# Se debe poder agregar funcionalidades sin cambiar el código fuente de la entidad

# En el siguiente ejemplo se muestra como la clase Notificar no incluye dentro
# de su código todas las formas para notificar al usuario algún evento
# Lo que se hace es crear varias clases que hereden de la clase Notificador
# Si el día de mañana queremos agregar notificaciones por twitter o instagram
# solo debemos agregar una clase NotificadorTwitter o NotificadorInstagram
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando email a {self.usuario.email}')


class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')


class NotificadorWTP(Notificador):
    def notificar(self):
        print(f'Enviado wtp a {self.usuario.whatsapp}')

