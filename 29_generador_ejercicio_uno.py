# Generador de números pares

def bucle_infinito():
  contador = 0
  while True:
    yield contador
    contador += 2

generador = bucle_infinito()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
