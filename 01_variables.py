# Variables
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. (Mala práctica)
name, surname, alias, age = "Jean", "Zambrano", "JP", 25
print("Me llamo:", name, surname, ". Mi edad es:", age, "y mi alias es:", alias)

# Inputs por teclado
# name = input("¿Cuál es tu primer nombre? ")
# age = int(input("¿Cuántos años tienes? "))

# print(name)
# print(age)

# Variables con tipo de dato (Falsas)
address: str = "Mi dirección"
address = 32

print(address)