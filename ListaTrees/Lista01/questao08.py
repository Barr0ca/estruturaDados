# Encontrando o valor mínimo em uma BST

from binarytree import bst

arvore = bst(height=2, is_perfect=True)

# Basicamente percorre até o canto mais a esquerda da árvore,
# caso não tenha mais valores à esquerda ele exibe o valor atual, que é o mínimo


def no_min(no):
    if no:
        no_min(no.left)
        if not no.left:
            print(no.value)


print(arvore)

no_min(arvore)
