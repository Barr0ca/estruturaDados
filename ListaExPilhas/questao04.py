def inverte_string(palavra: str):
    pilha = []
    str_invertida = ''
    for c in range((len(palavra)-1), -1, -1):
        pilha.append(palavra[c])
        str_invertida += pilha.pop()
    return str_invertida


palavra = 'ian'

print(inverte_string(palavra))
