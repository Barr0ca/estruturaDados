# Verificando palíndromos

def palindromo(nome: str):
    nomeInicial = nome
    if len(nome) == 0:
        if nome == nomeInicial:
            print('É palíndromo.')
        else:
            print('Não é palíndromo.')
    return nome[-1] + palindromo(nome[:-1])

palindromo('non')