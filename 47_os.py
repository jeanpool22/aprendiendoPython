import os

# Obtener directorio actual
cwd = os.getcwd()
print(f"Directorio de trabajo actual {cwd}")

# Listar los archivos .txt
txt_files = [f for f in os.listdir('./archivos') if f.endswith('.txt')]
print(f"Los archivos txt: {txt_files}")

os.rename('./archivos/cuento.txt', './archivos/caperucita.txt')
print("Archivo renombrado")

txt_files = [f for f in os.listdir('./archivos') if f.endswith('.txt')]
print(f"Los archivos txt: {txt_files}")