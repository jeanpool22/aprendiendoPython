# Impresión básica
print("Nunca pares de aprender")

# Uso de la coma en print, añade espacios
print("Nunca", "pares", "de", "aprender")

# Uso del operador + en print, no añade espacios
print("Nunca" + "pares" + "de" + "aprender")

# Uso del operador + en print añadiendo espacios
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# Uso de sep, especifica como separar los elementos contenidos dentro de un print
print("Nunca", "pares", "de", "aprender", sep=", ")

# Uso de end, cambia lo que se imprime al final de la llamada a print, por defecto tiene un salto de línea \n
print("Nunca", end=" ")
print("pares de aprender")

# Impresión de variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

# Uso del formato f-strings
print(f"Frase: {frase}, Autor: {author}")

# Uso del formato format
print("Frase: {}, Autor: {}".format(frase, author))

# Impresión con formato específico
valor = 3.14159
print("Valor: {:.2f}".format(valor))

# Saltos de línea y caracteres especiales
print("Hola\nmundo")
print("Hola soy \'Jean\'")
print("La ruta del archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")