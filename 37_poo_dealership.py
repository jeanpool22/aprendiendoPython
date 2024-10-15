class Car:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price
    self.is_available = True
  
  def sell(self):
    if self.is_available:
      self.is_available = False
      print(f"El coche {self.brand} {self.model} ha sido vendido.")
    else:
      print(f"El coche {self.brand} {self.model} no está disponible.")
    
  def check_available(self):
    return self.is_available

  def get_price(self):
    return self.price

class Customer:
  def __init__(self, name):
    self.name = name
    self.cars_purchased = []
  
  def buy_car(self, car):
    if car.check_available():
      car.sell()
      self.cars_purchased.append(car)
    else:
      print(f"Lo siento, {car.brand} {car.model} no está disponible.")
  
  def inquire_car(self, car):
    availability = "disponible" if car.check_available() else "no disponible"
    print(f"El coche {car.brand} {car.model} está {availability} y cuesta {car.price}")

class Dealership:
  def __init__(self):
    self.inventory = []
    self.customers = []
  
  def add_car(self, car):
    self.inventory.append(car)
    print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")

  def register_customer(self, customer):
    self.customers.append(customer)
    print(f"El cliente {customer.name} ha sido registrado en la concesionaria.")
  
  def show_available_cars(self):
    print("Coches disponibles en la concesionaria:")
    for car in self.inventory:
      if car.check_available():
        print(f"- {car.brand} {car.model} por {car.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

customer1 = Customer("Jean")

dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)

dealership.show_available_cars()

customer1.inquire_car(car1)

customer1.buy_car(car1)

dealership.show_available_cars()

customer1.buy_car(car1)