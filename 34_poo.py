class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Person("Jean", 25)
person2 = Person("Luis", 30)

person1.greet()
person2.greet()