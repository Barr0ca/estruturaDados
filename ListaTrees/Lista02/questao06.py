# Somando todos os valores de uma BST

from binarytree import bst

arvore = bst(height=2)


def soma_val_nos(no):
    if not no:  # Caso não exista nó atual retorna 0
        return 0
    # Soma o valor do nó atual a cada return
    return no.value + soma_val_nos(no.left) + soma_val_nos(no.right)


print(arvore)

print(soma_val_nos(arvore))
