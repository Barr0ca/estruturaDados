def palindromo(palavra):
    if len(palavra) <= 0:
        return f'É palíndromo'
    if palavra[-1] != palavra[0]:
        return f'Não é palíndromo'
    return palindromo(palavra[1:-1])


palavra = 'radar'
print(palindromo(palavra))
