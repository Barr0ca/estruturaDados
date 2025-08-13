def insertion(list, index):
    while index > 0:
        # Adicionando "[1]" para pegar o index 1 da tupla, nesse caso é a idade
        if list[index][1] < list[index - 1][1]:
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


tupla = [('ian', 20), ('Victor', 19), ('Cleide', 80),
         ('Bianca', 20), ('Bruno', 30)]

print(insertion_sort(tupla))
