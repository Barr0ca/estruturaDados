# Calculando a altura de uma BST

from binarytree import bst

arvore = bst(height=2)


def no_altura(no):
    if not no:  # Caso não exista mais nó retorna -1, seguindo a lógica da bibliota binarytree, uma árvore vazia tem tamanho -1
        return -1
    # Vai incrementar o número de vezes do maior ramo
    return 1 + max(no_altura(no.left), no_altura(no.right))


print(arvore)

print(no_altura(arvore))
