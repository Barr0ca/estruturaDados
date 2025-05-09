# Função que soma os N primeiros números naturais

def soma(n: int):
    if n == 0:
        return 0
    elif n < 0:
        return 'Essa função retorna apenas números positivos inteiros.'
    return n + soma(n-1)

res = soma(5)
print(res)