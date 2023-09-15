# ABRIR Y GUARDAR ARCHIVOS
# COMO ABRIR

# "w" es para escritura, si el archivo no existe lo crea, si existe lo sobreescribe
archivo = open("archivo.txt", "w", encoding="utf-8")  # Vamos a escribir un archivo
archivo.write("Texto de Prueba\n")
archivo.write("Segunda Linea\n")
archivo.close()

# "a" append es para añadir datos en un archivo
lista = ["Pepe", "Jose", "Genaro"]
archivo1 = open("archivo.txt", "a", encoding="utf-8")
archivo1.write(str(lista) + "\n")
archivo1.close()

# "r" es para lectura de un archivo
archivo_leer = open("archivo.txt", "r", encoding="utf-8")
#contenido = archivo_leer.read()
for linea in archivo_leer:
    print(linea)
archivo_leer.close()