import json

# Lectura del archivo
with open('./archivos/products.json', mode = 'r') as file:
  products = json.load(file)

# Mostrar el conternido
for product in products:
  #print(product)
  print(f"Product: {product['name']}, Price: {product['price']}")