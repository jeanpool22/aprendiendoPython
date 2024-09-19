add = lambda a, b: a + b
print(add(10, 4))

multiply = lambda a, b: a * b
print(multiply(4, 56))

numbers = range(11)
square_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Cuadrados: {square_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Pares: {even_numbers}")