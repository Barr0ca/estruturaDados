def palavras_duplicadas(lista: list):
    hashT = {}
    chaves = []
    resultado = []
    valores = []

    for palavra in lista: # Construção da hashtable
        chave = palavra # Toda palavra do texto ficará em minúscula
        if palavra not in hashT:
            hashT[chave] = 1
            chaves.append(chave) # Uma lista com todas as chaves
        else:
            hashT[chave] += 1 # Caso já exista uma chave ele incrementa o valor em +1
            
    for chave in chaves: # Separando em uma lista as palavras repetidas
        if hashT[chave] > 1:
            resultado.append(chave)

    for chave in chaves:
        valores.append(hashT[chave])

    valores = sorted(valores, reverse=True)

    for elemento in list(hashT):
        print(f'A palavra {elemento} apareceu {hashT[elemento]} vezes')


palavras_lower = []
texto = ' '
while texto != '':
    texto = input('texto:')
    palavras = texto.split()
    for palavra in palavras:
        palavras_lower.append(palavra.lower())

palavras_duplicadas(palavras_lower)