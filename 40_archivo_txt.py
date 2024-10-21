# Leer un archivo linea poir linea
"""with open('./archivos/cuento.txt', 'r') as file:
  for lineas in file:
    print(lineas.strip())"""

# Leer todas las líneas en una lista
"""with open('./archivos/cuento.txt', 'r') as file:
  lines = file.readlines()
  print(lines)"""

# Añadir texto
"""with open('./archivos/cuento.txt', 'a') as file:
  file.write("\n\nBy:ChatGPT")"""

# Sobreescribir el texto
with open('./archivos/cuento.txt', 'w') as file:
  file.write("\n\nBy:ChatGPT")