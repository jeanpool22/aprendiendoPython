import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sale = {}
with open('./archivos/monthly_sales.csv', mode='r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    month = row['month']
    sales = int(row['sales'])
    monthly_sale[month] = sales
  
sales = list(monthly_sale.values())

# Hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es {mean_sales}")

# Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es {median_sales}")

# Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es {mode_sales}")

# Desviación estándar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es {stdev_sales}")

# Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La variación es {variance_sales}")

# Extraer el máximo
max_sales = max(sales)

# Extraer el minimo
min_sales = min(sales)

# Rango
range_sales = max_sales - min_sales
print(f"Rango de ventas {range_sales}")