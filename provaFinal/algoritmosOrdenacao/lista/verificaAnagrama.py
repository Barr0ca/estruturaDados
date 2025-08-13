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


def verifica_anagrama(palavra01, palavra02):
    lista01 = []
    lista02 = []

    for letra in palavra01:
        lista01.append(letra)
    for letra in palavra02:
        lista02.append(letra)

    palavra01_ordenada = insertion_sort(lista01)
    palavra02_ordenada = insertion_sort(lista02)

    if palavra01_ordenada == palavra02_ordenada:
        return True
    else:
        return False


n1 = 'noiva'.lower()
n2 = 'navio'.lower()

if verifica_anagrama(n1, n2):
    print('São anagramas.')
else:
    print('Não são anagramas.')
