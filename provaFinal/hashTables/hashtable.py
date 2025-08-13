def num_duplicados(lista: list):
    ht = {}
    chaves = []
    resultado = []

    for elemento in lista:  # Construção da hashtable
        # Chaves podem ser strings: chave = str(elemento)
        if elemento not in ht:
            ht[elemento] = 1
            chaves.append(elemento)  # Uma lista com todas as chaves
        else:
            ht[elemento] += 1  # Caso já exista uma chave ele incrementa, duplicata

    for chave in chaves:  # Separando em uma lista as duplicatas
        if ht[chave] > 1:
            resultado.append(chave)

    return resultado


lista = [1, 1, 2, 3, 4, 5, 3, 5]
duplicados = num_duplicados(lista)
print(duplicados)
