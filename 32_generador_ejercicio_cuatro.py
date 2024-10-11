# Generador de números cuadrados

def numeros_cuadrados(limite):
  contador = 1
  while contador <= limite:
    yield contador ** 2
    contador += 1

generador = numeros_cuadrados(5)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))