# Função que retorna o enésimo (n) elemento da sequência de Fibonacci

def fibonacci(n):
   if n <= 2:
        return 1
   return fibonacci(n-1) + fibonacci(n-2)

res = fibonacci(6)
print(res)