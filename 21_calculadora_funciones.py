def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculator():
  while True:
    print("Seleccione una operación")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    option = int(input("Ingrese una opción (1, 2, 3, 4, 5): "))

    if option == 5:
      print("Saliendo de la calculadora")
      break
    
    if option in [1, 2, 3, 4]:
      num1 = float(input("Ingrese el primer número: "))
      num2 = float(input("Ingrese el segundo número: "))

      if option == 1:
        print(f"La suma es: {add(num1, num2)}")
      elif option == 2:
        print(f"La resta es: {substract(num1, num2)}")
      elif option == 3:
        print(f"La multiplicación es: {multiply(num1, num2)}")
      elif option == 4:
        print(f"La división es: {divide(num1, num2)}")
    
    else:
      print("Opción no válida, por favor intenta de nuevo")

calculator()