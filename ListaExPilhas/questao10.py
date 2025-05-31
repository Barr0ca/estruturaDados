def seq_numeros_palindromo(pilha: list):
    primeira_metade = pilha[:(len(pilha)//2)]
    segunda_metade = pilha[(len(pilha)//2):]  # Metade maior (inverte essa)
    pilha_comparativa = []

    if len(pilha) == 1:
        print('true')

    for i in range(len(segunda_metade)):
        pilha_comparativa.append(segunda_metade.pop())

    if len(pilha_comparativa) > len(primeira_metade):
        pilha_comparativa.pop()


    for a in range(-1, len(primeira_metade)-1):
        if primeira_metade[a] == pilha_comparativa[a]:
            return True
        else:
            return False


pilha = [1, 2, 2, 1]
if seq_numeros_palindromo(pilha):
    print('Forma um palíndromo.')
else:
    print('Não forma um palíndromo.')
