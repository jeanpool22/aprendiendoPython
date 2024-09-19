def factorial(n):
  if n == 0:
    return 1
  
  return n * factorial(n - 1)

factorial_5 = factorial(5)
print(factorial_5)

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

number = 4
print([fibonacci(n) for n in range(5)])

def natural(n):
  if n == 1:
    return 1
  return n + natural(n - 1)

add_natural = 6
print(natural(add_natural))