# Contando as folhas de uma BST

from binarytree import bst

arvore = bst(height=2)


def conta_nos_folhas(no):
    if not no:  # Caso não tenha no retorna 0
        return 0
    if not no.left and not no.right:  # Caso o nó atual não tenha filho nem à sua esquerda e nem a sua direita é uma folha
        return 1  # Incrementa + 1
    # Soma os valores encontrados nos ramos
    return conta_nos_folhas(no.left) + conta_nos_folhas(no.right)


print(arvore)

print(conta_nos_folhas(arvore))
