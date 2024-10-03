#Implementa un iterador que recorra una lista de elementos de manera cíclica infinita, 
# es decir, cuando llegue al final de la lista, comience de nuevo desde el principio.
class Contador:
  def __init__(self, lista):
    self.lista = lista
    self.actual = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.actual < len(self.lista):
      resultado = self.lista[self.actual]
      self.actual += 1
    else:
      self.actual = 0
      resultado = self.lista[self.actual]
      self.actual += 1
    return resultado
  
contador = Contador(range(1, 6))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))