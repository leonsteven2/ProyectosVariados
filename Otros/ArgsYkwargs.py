# Cuando se especifica *args en una función quiere decir que
# Va a recibir n argumentos dentro de la función
# la variable args guardara en una tupla todos los argumentos que se pasen a la función
def funcion(*args):
    print(args)
    for arg in args:
        print(arg)


funcion(1, "2", [1, 2, 3], "hola", 5.0)


# **kwargs
# En este caso se debe especificar al llamar la función, la llave y valor de los argumentos
# **kwargs almacena en un diccionario la llave y valor
def empleado(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


empleado(nombre="carlos", puesto="programador", lenguaje="java")
