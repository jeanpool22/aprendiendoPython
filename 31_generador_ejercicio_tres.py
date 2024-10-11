#Generador de sublistas

def sublistas(lista):
  lista_alterna = []
  for i in range(len(lista)):
    lista_alterna.append(lista[i])
    yield lista_alterna

lista = [1, 2, 3, 4, 5]
generador = sublistas(lista)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))