#Generador de la secuencia Fibonacci

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

generador = fibonacci()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))