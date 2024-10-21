import csv

# Leer un archivo
"""with open('./archivos/products.csv', mode='r') as file:
  csv_reader = csv.DictReader(file)
  for row in csv_reader:
    print(row)"""

# Mostrar la información por columnas
with open('./archivos/products.csv', mode='r') as file:
  csv_reader = csv.DictReader(file)
  for row in csv_reader:
    print(f"Producto: {row['name']}, Precio: {row['price']}")