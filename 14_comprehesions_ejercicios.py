# Crea una lista que contenga solo los números que son mayores que 10 y que sean divisibles por 3.
numeros = [5, 12, 18, 23, 7, 15, 9]
numbers = [n for n in numeros if n > 10 and n % 3 == 0]
print(numbers)

# Crea un conjunto que contenga todas las palabras que tienen más de 5 letras.
palabras = ["python", "comprehension", "list", "code", "exercise", "simple"]
words = {word for word in palabras if len(word) > 5}
print(words)

# Crea un diccionario donde cada clave sea una cadena y cada valor sea la longitud de esa cadena.
cadenas = ["apple", "banana", "cherry", "date", "elderberry"]
strings = {fruta: len(fruta) for fruta in cadenas}
print(strings)

# Crea una lista de nombres de las personas que tienen 18 años o más.
personas = [("Ana", 22), ("Juan", 17), ("Luis", 20), ("Pedro", 16)]
people = [persona[0] for persona in personas if persona[1] >= 18]
print(people)

# Crea una lista de listas donde cada sublista contenga los dígitos de cada número en la lista original.
numeros_dos = [123, 456, 789]
numbers_dos = [[int(digito) for digito in str(numero)] for numero in numeros_dos]
print(numbers_dos)

# Dada una lista de frases, crea una lista de las palabras que tienen exactamente 4 letras. Considera que las palabras están separadas por espacios.
frases = ["The quick brown fox", "jumps over the lazy dog", "Hello world"]
list_sentences = [n for n in " ".join(frases).split() if len(n) == 4]
print(list_sentences)

# Dada una lista de números, crea un conjunto que contenga los cuadrados de los números que son menores de 10.
numeros_tres = [1, 4, 9, 16, 25, 36]
numbers_tres = {n**2 for n in numeros_tres if n < 10}
print(numbers_tres)

# Dada una lista de listas, donde cada lista interna contiene dos números, crea una lista de las sumas de cada pareja de números.
pares = [[1, 2], [3, 4], [5, 6], [7, 8]]
pares_suma = [par[0] + par[1] for par in pares]
print(pares_suma)

# Dada una lista de números enteros, crea una lista de cadenas donde cada cadena representa el número en formato binario, sin el prefijo '0b'.
numeros_cuatro = [2, 5, 8, 10]
numeros_binarios = [bin(n)[2:] for n in numeros_cuatro]
print(numeros_binarios)