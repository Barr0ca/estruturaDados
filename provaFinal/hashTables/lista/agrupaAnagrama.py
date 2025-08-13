def insertion(list, index):
    while index > 0:
        if list[index] < list[index - 1]:
            aux = list[index]
            list[index] = list[index - 1]
            list[index - 1] = aux
        index -= 1
    return list


def insertion_sort(list):
    i = 1
    while i < len(list):
        insertion(list, i)
        i += 1
    return list


def ordena_palavra(palavra):
    lista = []
    palavra_ordenada = ''

    for letra in palavra:
        lista.append(letra)

    lista_letras_ordenadas = insertion_sort(lista)

    for letra in lista_letras_ordenadas:
        palavra_ordenada += letra

    return palavra_ordenada


def anagramas(palavras: list):
    frequencia_anagramas = {}

    for palavra in palavras:
        palavra_o = ordena_palavra(palavra)

        if palavra_o in frequencia_anagramas:
            frequencia_anagramas[palavra_o].append(palavra)
        else:
            frequencia_anagramas[palavra_o] = [palavra]

    return frequencia_anagramas


palavras = ['amor', 'roma', 'risonho', 'calieupto', 'eucalipto', 'batata']

print(anagramas(palavras))
