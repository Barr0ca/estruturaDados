# Função que retorna o fatorial de um número inteiro positivo

def fatorial(n):
  if n == 1:
    return 1
  if n < 0:
    return 'Essa função retorna apenas números positivos inteiros.'
  return n * fatorial(n-1)

res = fatorial(5)
print(res)