# Verificando palíndromos

def palindromo(nome: str):
    if len(nome) <= 1:
        return f'É Palíndromo'
    if nome[0] != nome[-1]:
        return f'Não é palíndromo'
    return palindromo(nome[1:-1])

print(palindromo('aba'))
