# Remoção em uma BST

from binarytree import bst

arvore = bst(height=2)


def encontrar_index(no, valor):  # Função que encontra o index equivalente ao valor fornecido
    contador = 0
    for i in no:  # Loop para incrementar o contador até chegar ao valor
        if i.value == valor:
            return contador  # Index do valor
        contador += 1
    return None


def remove(no, index):  # Função que utiliza del para deletar por index o valor
    if index is None:
        return 'Valor não encontrado.'
    del no[index]
    return no


index = encontrar_index(arvore, 0)

print(arvore)

print(remove(arvore, index))
