from binarytree import bst, Node

arvore = bst(height=2)


def no_altura(no):
    if not no:
        return -1
    return 1 + max(no_altura(no.left), no_altura(no.right))


print(arvore)

print(no_altura(arvore))
