# Implementa un iterador que recorra los números del 1 al 100, pero solo devuelva aquellos 
# que sean divisibles por 3. Si un número no es divisible por 3, lo debe saltar.
class Contador:
  def __init__(self, lista):
    self.lista = lista
    self.indice = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    while self.indice < len(self.lista):
      resultado = self.lista[self.indice]
      self.indice += 1
      if resultado % 3 == 0:
        return resultado
    raise StopIteration
    
contador = Contador(range(1, 101))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))