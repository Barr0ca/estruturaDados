def palindromo(palavra: str):
    primeira_metade = palavra[:(len(palavra)//2)]
    segunda_metade = palavra[(len(palavra)//2):]  # Metade maior (inverte essa para poder retirar seu elemento que sobra. Ex.: 'teclado' = 'tec' e 'lado' retira 'l' que é o elemento do meio, para palíndromo é indiferente.)
    pilha_comparativa = [] # Usar essa pilha para comparar os primeiros elementos de cada pilha.
    transforma_pilha = [] # Armazenar os elementos da string nessa pilha.

    if len(palavra) == 1: # Str tamanho 1 é palíndromo
        print(True)

    for i in range(len(segunda_metade)): # Metade maior (sempre a segunda) invertida para poder comparar com a primeira metade. 
        pilha_comparativa.append(segunda_metade[i])

    for i in range(len(primeira_metade)): # Armazenando valores da string aqui.
        transforma_pilha.append(primeira_metade[i])

    # Nesse if eu armazeno na pilha comparativa os valores da segunda metade excluindo o valor excedente, que eu mencionei que é indiferente para palíndromos. 
    if len(pilha_comparativa) > len(transforma_pilha): 
        pilha_comparativa = []
        for i in range(len(transforma_pilha)):
            pilha_comparativa.append(segunda_metade[i])


    # Nesse for eu comparo cada primeiro elemento das duas pilhas (primeira metade e a pilha comparativa, segunda metade), caso em uma ocorrencia isso seja falso o programa para e retorna false.
    for a in range(-1, len(primeira_metade)-1):
        if primeira_metade[a] == pilha_comparativa[a]:
            return True
        else:
            return False

palavra = 'radar'
palavra2 = 'teclado'
print(palindromo(palavra))
print(palindromo(palavra2))