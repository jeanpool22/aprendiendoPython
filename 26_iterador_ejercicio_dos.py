# Iterador personalizado para n-repeticiones
class Contador:
  def __init__(self, lista, repeticion):
    self.lista = lista
    self.repeticion_total = repeticion
    self.repeticion_actual = repeticion
    self.actual = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.actual < len(self.lista):
      if self.repeticion_actual > 0:
        resultado = self.lista[self.actual]
        self.repeticion_actual -= 1
        return resultado
      else:
        self.actual += 1
        if self.actual < len(self.lista):
          self.repeticion_actual = self.repeticion_total
          return self.__next__()
        else:
          raise StopIteration
    else:
      raise StopIteration

lista = [1, 2, 3, 4, 5]
repeticion = 3
contador = Contador(lista, repeticion)
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