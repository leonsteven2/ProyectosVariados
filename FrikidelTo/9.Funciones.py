import time

# Se pueden utilizar variables globales (num3) dentro de una función
# Pero no se puede modificar las variables globales (num3) dentro de una función
# def sumar(num1, num2):
#     num3 = 5
#     print(f'num3 en la función es: {num3}')
#     return num1 + num2
#
#
# num3 = 10
# resultado = sumar(4, 5)
# print(resultado)
# print(f'num3 en el programa: {num3}')


# Para modificar la variable global se debe añadir
# global <<variable>> dentro de la función
# def sumar(num1, num2):
#     global num3
#     num3 = 5
#     print(f'num3 en la función es: {num3}')
#     return num1 + num2
#
# resultado = sumar(4, 5)
# print(f'num3 en el programa: {num3}')


# Se puede establecer valores por defecto en una función
# def sumar(num1=5, num2=7):
# Solo se utilizan cuando se llama la función sin ningún parámetro
# resultado = sumar() or sumar(1) <- En este caso num1=1


# Las funciones que no retornan nada, retornaran none


# Se puede establecer el valor de los parámetros de la función
# resultado = sumar(num2=5)
# resultado = sumar(num1=2)
# Los parámetros no definidos tomarán el valor por defecto si tuviera
# Caso contrario, saltará una excepción
