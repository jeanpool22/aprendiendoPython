# Generador con retardo controlado
import time

def retardo():
  contador = 0
  while True:
    yield contador
    contador += 1
    time.sleep(1)


generador = retardo()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))