# Iterador de una lista inversa
class Contador:
  def __init__(self, lista):
    self.lista = lista
    self.indice = len(self.lista)

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.indice > 0:
      resultado = self.lista[self.indice - 1]
      self.indice -= 1
      return resultado
    else:
      raise StopIteration
    
mi_lista = [1, 2, 3, 4, 5]
iterador = Contador(mi_lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))