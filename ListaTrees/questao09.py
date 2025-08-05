from binarytree import bst, Node

arvore = bst(height=2, is_perfect=True)


def no_max(no):
    if no:
        no_max(no.right)
        if no.right is None:
            print(no.value)


print(arvore)

no_max(arvore)
