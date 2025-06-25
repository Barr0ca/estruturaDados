# Verifica a frequencia de uma palavra em um texto

def palavras_duplicadas(lista: list):
    hashT = {}
    chaves = []
    resultado = []

    for palavra in lista: # Construção da hashtable
        chave = str.lower(palavra) # Toda palavra do texto ficará em minúscula
        if palavra not in hashT:
            hashT[chave] = 1
            chaves.append(chave) # Uma lista com todas as chaves
        else:
            hashT[chave] += 1 # Caso já exista uma chave ele incrementa o valor em +1
            
    for chave in chaves: # Separando em uma lista as palavras repetidas
        if hashT[chave] > 1:
            resultado.append(chave)

    for duplicata in resultado: # Um for para exibir a palavra (chave) e seu valor (número de vezes que repete)
        print(f'A palavra "{duplicata}" apareceu {hashT[duplicata]} vezes.')

texto = 'O rato roeo a roupa do rei de roma em roma o rato roeo'
palavras = texto.split() # Transformando o texto em uma lista de palavras (as palavras se tornam elementos da lista, a função divide as palavras pelos espaços)

duplicatas = palavras_duplicadas(palavras)

