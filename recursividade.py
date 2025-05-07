# import time

def fatorial(n):
  if n == 1:
    return 1
  return n * fatorial(n-1)

# inicio = time.time()
# res = fatorial(999)
# fim = time.time()
# print(f'tempo de execução: {(fim-inicio):.2} segundos')

def potencia(n,p):
    if p == 0:
        return 1
    return n * potencia(n, p-1)

# print(potencia(-3, 3))

def fibonacci(n):
   if n <= 2:
        return 1
   return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))