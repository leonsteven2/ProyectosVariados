# Los decoradores toman una función como entrada
# Le agregan una funcionalidad extra
# Y devuelve la función modificada (sin cambiar la función original)

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()

    return funcion_modificada


# CÓDIGO NO ÓPTIMO
# def funcion_principal():
#     print("Hola desde la función principal")
#
#
# funcion_modificada_main = decorador(funcion_principal)
# funcion_modificada_main()

# CÓDIGO ÓPTIMO
@decorador
def funcion_principal():
    print("Hola desde la función principal")


funcion_principal()
