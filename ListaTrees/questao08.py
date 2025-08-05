from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def no_min(no):
    if no:
        no_min(no.left)
        if no.left is None:
            print(no.value)


print(arvore)

no_min(arvore)
