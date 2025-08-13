def inverte(palavra: str):
    pilha = []
    palavra_invertida = ''

    for letra in palavra:
        pilha.append(letra)

    for i in range(len(pilha)):
        palavra_invertida += pilha.pop()

    print(palavra_invertida)


inverte('botafogo')
