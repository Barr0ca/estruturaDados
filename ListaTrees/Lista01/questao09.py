# Encontrando o valor máximo em uma BST

from binarytree import bst

arvore = bst(height=2, is_perfect=True)

# Basicamente percorre até o canto mais a direita da árvore,
# caso não tenha mais valores à direita ele exibe o valor atual, que é o máximo


def no_max(no):
    if no:
        no_max(no.right)
        if no.right is None:
            print(no.value)


print(arvore)

no_max(arvore)
